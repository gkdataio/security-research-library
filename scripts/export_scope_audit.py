#!/usr/bin/env python3
"""Reconcile canonical program scopes with both catalogs and their pages offline."""

import argparse
from collections import Counter
import json

from build_navigation import link, text
from export_bugcrowd_programs import build as build_bugcrowd
from export_program_discovery import build as build_discovery
from export_programs import build as build_programs
from export_public_bounties import build as build_bounties
from validate import ROOT, Invalid


def _read(root, name):
    return json.loads((root / name).read_text(encoding="utf-8"))


def _expect(condition, message):
    if not condition:
        raise Invalid("scope audit: " + message)


def _candidate_ids(listings, captures, verified):
    chosen = set()
    for listing in listings:
        policy = verified.get(listing["verified_policy_id"])
        capture = captures.get(listing["id"])
        policy_type = policy.get("program_type", {}).get("value") if policy else None
        if policy_type == "vulnerability_disclosure" or (capture and capture["status"] == "not_paid_bounty"):
            continue
        if (policy_type == "paid_bounty"
                or (listing["platform"] == "HackerOne" and capture and capture.get("offers_bounties") is True)
                or listing["program_type"] == "paid_bounty"
                or (listing["platform"] == "Bugcrowd" and listing["program_type"] == "unknown")):
            chosen.add(listing["id"])
    return chosen


def _canonical_bounty_scope(listing, captures, verified):
    policy = verified.get(listing["verified_policy_id"])
    if policy and policy.get("asset_scope"):
        scope = policy["asset_scope"]
        return "captured", scope["in_scope"], scope["out_of_scope"]
    capture = captures.get(listing["id"])
    if capture is None:
        return "not_attempted", [], []
    assets = capture.get("assets", []) if capture["status"] == "captured" else []
    return (capture["status"],
            [{k: v for k, v in row.items() if k != "scope"} for row in assets if row["scope"] == "in"],
            [{k: v for k, v in row.items() if k != "scope"} for row in assets if row["scope"] == "out"])


def build(root=ROOT):
    program_outputs = build_programs(root)
    discovery_outputs = build_discovery(root)
    bounty_outputs = build_bounties(root)
    bugcrowd_outputs = build_bugcrowd(root)
    verified = json.loads(program_outputs["exports/programs.json"])
    discovery = json.loads(discovery_outputs["exports/program-discovery.json"])
    bounty = json.loads(bounty_outputs["exports/public-bounties.json"])
    bugcrowd = json.loads(bugcrowd_outputs["exports/bugcrowd-programs.json"])
    raw_bounty = _read(root, "data/public-bounty-scopes.json")["captures"]
    raw_vdp = _read(root, "data/bugcrowd-vdp-scopes.json")["captures"]
    verified_by_id = {item["id"]: item for item in verified["programs"]}
    listings = {item["id"]: item for item in discovery["listings"]}
    bounty_captures = {item["listing_id"]: item for item in raw_bounty}
    vdp_captures = {item["listing_id"]: item for item in raw_vdp}
    bounty_by_id = {item["id"]: item for item in bounty["programs"]}
    bugcrowd_by_id = {item["id"]: item for item in bugcrowd["programs"]}
    _expect(len(bounty_captures) == len(raw_bounty) and len(vdp_captures) == len(raw_vdp),
            "duplicate canonical capture ID")
    _expect(len(bounty_by_id) == len(bounty["programs"]) and len(bugcrowd_by_id) == len(bugcrowd["programs"]),
            "duplicate catalog ID")
    _expect(set(bounty_by_id) == _candidate_ids(listings.values(), bounty_captures, verified_by_id),
            "bounty candidate IDs differ from canonical classification evidence")
    latest = max((batch for batch in discovery["batches"] if batch["platform"] == "Bugcrowd"),
                 key=lambda batch: batch["reviewed_at"])
    current = _read(root, "data/program-discovery/" + latest["id"] + ".json")
    _expect(set(bugcrowd_by_id) == {entry["id"] for entry in current["entries"]},
            "Bugcrowd catalog does not cover the latest public directory batch")
    _expect(bugcrowd["directory_snapshot_date"] == latest["reviewed_at"][:10],
            "Bugcrowd catalog date differs from the source batch")

    for ident, row in bounty_by_id.items():
        status, included, excluded = _canonical_bounty_scope(listings[ident], bounty_captures, verified_by_id)
        _expect((row["scope_status"], row["in_scope"], row["out_of_scope"]) ==
                (status, included, excluded), "bounty scope differs from canonical rows: " + ident)
    overlap = set(bounty_by_id) & set(bugcrowd_by_id)
    for ident, row in bugcrowd_by_id.items():
        if ident in overlap:
            other = bounty_by_id[ident]
            _expect((row["scope_status"], row["in_scope"], row["out_of_scope"]) ==
                    (other["scope_status"], other["in_scope"], other["out_of_scope"]),
                    "overlapping catalog scope differs: " + ident)
        else:
            capture = vdp_captures.get(ident)
            _expect(capture is not None and row["directory_category"] == "vdp",
                    "Bugcrowd-only listing lacks canonical VDP capture: " + ident)
            assets = capture.get("assets", []) if capture["status"] == "captured" else []
            included = [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "in"]
            excluded = [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "out"]
            _expect((row["scope_status"], row["in_scope"], row["out_of_scope"]) ==
                    (capture["status"], included, excluded), "VDP scope differs from canonical rows: " + ident)

    union = dict(bounty_by_id)
    union.update(bugcrowd_by_id)
    gaps = [item for item in union.values() if item["scope_status"] != "captured"]
    _expect(all(item.get("gap_review") for item in gaps), "an unresolved gap lacks an official-page review")
    for item in union.values():
        page = item.get("visual_page") or ("docs/public-bounties/" + item["platform"].lower() +
                                           "/" + item["id"] + ".md")
        content = bugcrowd_outputs.get(page) or bounty_outputs.get(page)
        _expect(content is not None, "missing generated program page: " + page)
        _expect("In-scope entries (" + str(len(item["in_scope"])) + ")" in content,
                "generated in-scope heading differs from JSON: " + item["id"])
        _expect("Out-of-scope entries (" + str(len(item["out_of_scope"])) + ")" in content,
                "generated out-of-scope heading differs from JSON: " + item["id"])

    status_counts = dict(sorted(Counter(item["scope_status"] for item in union.values()).items()))
    duplicate_rows = sum(item.get("duplicate_source_rows", 0) for item in raw_bounty + raw_vdp)
    counts = {
        "verified_policy_records": len(verified_by_id),
        "verified_with_asset_scope": sum(bool(item.get("asset_scope")) for item in verified_by_id.values()),
        "verified_in_scope_rows": sum(len(item["asset_scope"]["in_scope"]) for item in verified_by_id.values()
                                       if item.get("asset_scope")),
        "verified_out_of_scope_rows": sum(len(item["asset_scope"]["out_of_scope"]) for item in verified_by_id.values()
                                           if item.get("asset_scope")),
        "discovery_listings": len(listings),
        "discovery_verified_policy_overlap": discovery["counts"]["already_has_verified_policy"],
        "discovery_scope_tables_captured": discovery["counts"]["public_scope_tables_captured"],
        "raw_bounty_capture_records": len(raw_bounty),
        "raw_vdp_capture_records": len(raw_vdp),
        "bugcrowd_public_listings": len(bugcrowd_by_id),
        "bugcrowd_scope_captured": bugcrowd["counts"]["published_scope_captured"],
        "bugcrowd_scope_gaps": bugcrowd["counts"]["scope_gaps"],
        "bugcrowd_in_scope_rows": sum(len(item["in_scope"]) for item in bugcrowd_by_id.values()),
        "bugcrowd_out_of_scope_rows": sum(len(item["out_of_scope"]) for item in bugcrowd_by_id.values()),
        "cross_platform_bounty_candidates": len(bounty_by_id),
        "bounty_by_platform": dict(sorted(Counter(item["platform"] for item in bounty_by_id.values()).items())),
        "bounty_scope_captured": bounty["counts"]["with_published_scope"],
        "bounty_scope_gaps": bounty["counts"]["scope_not_captured"],
        "bounty_in_scope_rows": sum(len(item["in_scope"]) for item in bounty_by_id.values()),
        "bounty_out_of_scope_rows": sum(len(item["out_of_scope"]) for item in bounty_by_id.values()),
        "catalog_overlap": len(overlap),
        "distinct_catalog_programs": len(union),
        "distinct_scope_captured": status_counts.get("captured", 0),
        "distinct_scope_gaps": len(gaps),
        "distinct_in_scope_rows": sum(len(item["in_scope"]) for item in union.values()),
        "distinct_out_of_scope_rows": sum(len(item["out_of_scope"]) for item in union.values()),
        "duplicate_source_rows_collapsed": duplicate_rows,
        "by_gap_status": {status: count for status, count in status_counts.items() if status != "captured"},
        "by_gap_result": dict(sorted(Counter(item["gap_review"]["result"] for item in gaps).items())),
        "gap_pages_reviewed": len(gaps),
    }
    _expect(len(overlap) == bugcrowd["counts"]["bug_bounty_category"],
            "overlap is not exactly the Bugcrowd bounty category")
    _expect(counts["discovery_listings"] == discovery["counts"]["unique_program_page_listings"],
            "discovery count differs from exported listings")
    _expect(counts["verified_policy_records"] == verified["counts"]["programs"],
            "verified policy count differs from export")
    _expect((counts["verified_with_asset_scope"], counts["verified_in_scope_rows"],
             counts["verified_out_of_scope_rows"]) ==
            (verified["counts"]["programs_with_asset_scope"], verified["counts"]["in_scope_entries"],
             verified["counts"]["out_of_scope_entries"]), "verified scope rows differ from export")
    _expect(counts["discovery_verified_policy_overlap"] ==
            sum(bool(item["verified_policy_id"]) for item in listings.values()),
            "discovery verified-policy overlap differs from listings")
    _expect(counts["discovery_listings"] - counts["discovery_verified_policy_overlap"] ==
            discovery["counts"]["awaiting_policy_review"], "discovery review queue differs from listings")
    _expect(counts["bounty_by_platform"] == bounty["counts"]["by_platform"],
            "bounty platform counts differ from export")
    _expect((counts["cross_platform_bounty_candidates"], counts["bounty_scope_captured"],
             counts["bounty_scope_gaps"]) ==
            (bounty["counts"]["observed_bounty_candidates"],
             bounty["counts"]["by_scope_status"].get("captured", 0),
             sum(count for status, count in bounty["counts"]["by_scope_status"].items()
                 if status != "captured")), "bounty totals differ from exported status counts")
    _expect((counts["bugcrowd_public_listings"], counts["bugcrowd_scope_captured"],
             counts["bugcrowd_scope_gaps"]) ==
            (bugcrowd["counts"]["current_public_programs"],
             bugcrowd["counts"]["by_scope_status"].get("captured", 0),
             sum(count for status, count in bugcrowd["counts"]["by_scope_status"].items()
                 if status != "captured")), "Bugcrowd totals differ from exported status counts")
    _expect((counts["bounty_in_scope_rows"], counts["bounty_out_of_scope_rows"]) ==
            (bounty["counts"]["in_scope_entries"], bounty["counts"]["out_of_scope_entries"]),
            "bounty scope rows differ from export")
    _expect((counts["bugcrowd_in_scope_rows"], counts["bugcrowd_out_of_scope_rows"]) ==
            (bugcrowd["counts"]["in_scope_entries"], bugcrowd["counts"]["out_of_scope_entries"]),
            "Bugcrowd scope rows differ from export")
    _expect(counts["duplicate_source_rows_collapsed"] ==
            bounty["counts"]["duplicate_source_rows_removed"] +
            sum(vdp_captures[ident].get("duplicate_source_rows", 0) for ident in set(bugcrowd_by_id) - overlap),
            "collapsed row count differs from catalog attribution")
    _expect(counts["discovery_scope_tables_captured"] ==
            sum(item["status"] == "captured" for item in raw_bounty + raw_vdp),
            "discovery scope-table count differs from canonical captures")
    _expect(counts["distinct_scope_captured"] + counts["distinct_scope_gaps"] ==
            counts["distinct_catalog_programs"], "distinct scope statuses do not cover the union")
    _expect(counts["bounty_scope_captured"] + counts["bugcrowd_scope_captured"] -
            sum(bounty_by_id[ident]["scope_status"] == "captured" for ident in overlap) ==
            counts["distinct_scope_captured"], "captured scopes differ after overlap removal")

    gap_records = sorted(({
        "id": item["id"], "name": item["name"], "platform": item.get("platform", "Bugcrowd"),
        "status": item["scope_status"], "visual_page": item.get("visual_page") or
        "docs/public-bounties/" + item["platform"].lower() + "/" + item["id"] + ".md",
        "gap_review": item["gap_review"],
    } for item in gaps), key=lambda item: (item["platform"], item["name"].casefold(), item["id"]))
    notice = ("Counts cover dated public directory snapshots and published scope rows. "
              "A visible listing or captured table is not a complete policy review or authorization to test. "
              "Empty exclusions do not mean unrestricted scope.")
    export = {"schema_version": "1.0.0", "bugcrowd_snapshot_date": bugcrowd["directory_snapshot_date"],
              "notice": notice, "counts": counts, "unresolved_gaps": gap_records}
    lines = ["# Program scope coverage audit", "",
             "[Library home](../README.md) · [Bugcrowd catalog](bugcrowd-programs.md) · "
             "[Bounty catalog](public-bounties.md) · [Discovery queue](program-discovery.md)", "",
             notice, "", "## Reconciled counts", "",
             "| Measure | Count |", "| --- | ---: |",
             f"| Separately reviewed policy records | {counts['verified_policy_records']} |",
             f"| Reviewed policy in-scope / out-of-scope rows | {counts['verified_in_scope_rows']} / {counts['verified_out_of_scope_rows']} |",
             f"| Discovery program-page listings | {counts['discovery_listings']} |",
             f"| Discovery listings linked to reviewed policies | {counts['discovery_verified_policy_overlap']} |",
             f"| Discovery listings with captured public scope tables | {counts['discovery_scope_tables_captured']} |",
             f"| Raw bounty / VDP capture records | {counts['raw_bounty_capture_records']} / {counts['raw_vdp_capture_records']} |",
             f"| Bugcrowd public listings | {counts['bugcrowd_public_listings']} |",
             f"| Bugcrowd published scope captured | {counts['bugcrowd_scope_captured']} |",
             f"| Bugcrowd scope gaps | {counts['bugcrowd_scope_gaps']} |",
             f"| Bugcrowd in-scope / out-of-scope rows | {counts['bugcrowd_in_scope_rows']} / {counts['bugcrowd_out_of_scope_rows']} |",
             f"| Cross-platform bounty candidates | {counts['cross_platform_bounty_candidates']} |",
             f"| Bounty published scope captured | {counts['bounty_scope_captured']} |",
             f"| Bounty scope gaps | {counts['bounty_scope_gaps']} |",
             f"| Bounty in-scope / out-of-scope rows | {counts['bounty_in_scope_rows']} / {counts['bounty_out_of_scope_rows']} |",
             f"| Overlapping Bugcrowd bounty listings | {counts['catalog_overlap']} |",
             f"| Distinct programs across both catalogs | {counts['distinct_catalog_programs']} |",
             f"| Distinct programs with captured scope rows | {counts['distinct_scope_captured']} |",
             f"| Distinct unresolved scope gaps | {counts['distinct_scope_gaps']} |",
             f"| Distinct in-scope rows | {counts['distinct_in_scope_rows']} |",
             f"| Distinct out-of-scope rows | {counts['distinct_out_of_scope_rows']} |",
             f"| Repeated source rows collapsed | {counts['duplicate_source_rows_collapsed']} |", "",
             f"The {counts['catalog_overlap']} overlapping Bugcrowd bounty pages are counted once in the distinct totals. "
             f"The {counts['verified_policy_records']} separately reviewed policies include "
             f"{bounty['counts']['verified_policy_records']} bounty-catalog records; they are not added again. "
             "The October 3 Bugcrowd snapshot is paired with the earlier HackerOne and Intigriti directory observations.", "",
             "## Unresolved gaps", "",
             f"Official pages showed {counts['by_gap_result'].get('preview_login_gate', 0)} preview login gates, "
             f"{counts['by_gap_result'].get('terms_login_gate', 0)} terms login gates, "
             f"{counts['by_gap_result'].get('empty_published_table', 0)} empty public tables, "
             f"{counts['by_gap_result'].get('javascript_required', 0)} JavaScript shells without an independently visible asset list, "
             f"and {counts['by_gap_result'].get('http_403', 0)} HTTP 403 responses.", "",
             "| Program | Platform | Status | Official policy review |", "| --- | --- | --- | --- |"]
    for item in gap_records:
        page = item["visual_page"].removeprefix("docs/")
        lines.append("| " + link(item["name"], page) + " | " + text(item["platform"]) + " | " +
                     text(item["status"].replace("_", " ")) + " | " +
                     link(item["gap_review"]["result"].replace("_", " "),
                          item["gap_review"]["policy_url"]) + " |")
    lines += ["", "Each gap page states the observed access or asset-list limitation. "
              "The [JSON audit](../exports/program-scope-audit.json) retains the exact review note and timestamp.", ""]
    return {"exports/program-scope-audit.json": json.dumps(export, indent=2, ensure_ascii=False) + "\n",
            "docs/program-scope-audit.md": "\n".join(lines)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for name, content in build().items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise SystemExit("Missing or stale scope audit output: " + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print("Canonical scope counts, catalog overlap, gap reviews and pages reconciled (offline).")


if __name__ == "__main__":
    main()
