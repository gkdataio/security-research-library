#!/usr/bin/env python3
"""Validate and render the current public Bugcrowd program and scope catalog offline."""

import argparse
from collections import Counter
import json
from urllib.parse import urlsplit

from build_navigation import link, text
from export_program_discovery import build as build_discovery
from export_public_bounties import build as build_bounties, render_asset_table
from validate import ROOT, Invalid, check_schema


STATUS_LABELS = {
    "captured": "Published scope captured",
    "no_published_assets": "No published asset rows found",
    "fetch_failed": "Scope fetch failed",
    "not_attempted": "Scope not yet fetched",
}
OFFICIAL_HOSTS = {"bugcrowd.com", "eu.bugcrowd.net", "gov.bugcrowd.net"}


def load_vdp_captures(root, current, snapshot_date):
    path = root / "data/bugcrowd-vdp-scopes.json"
    schema = json.loads((root / "schema/bugcrowd-vdp-scopes.schema.json").read_text(encoding="utf-8"))
    data = json.loads(path.read_text(encoding="utf-8"))
    check_schema(data, schema, schema)
    if data["directory_snapshot_date"] != snapshot_date:
        raise Invalid("Bugcrowd VDP captures identify a different directory snapshot")
    captures = {}
    for item in data["captures"]:
        ident = item["listing_id"]
        if ident in captures:
            raise Invalid("duplicate Bugcrowd VDP capture ID: " + ident)
        listing = current.get(ident)
        if not listing or listing["program_type"] != "vulnerability_disclosure":
            raise Invalid("VDP capture is absent from current Bugcrowd directory: " + ident)
        if any(item[key] != listing[key] for key in ("name", "program_url")):
            raise Invalid("VDP capture identity differs from directory listing: " + ident)
        source = item.get("source_url")
        if source and urlsplit(source).hostname not in OFFICIAL_HOSTS:
            raise Invalid("VDP scope source is not on Bugcrowd: " + ident)
        if item["status"] == "captured" and (not item.get("assets") or not source):
            raise Invalid("captured VDP requires published assets and official source: " + ident)
        if item["status"] == "no_published_assets" and (item.get("assets") or not source):
            raise Invalid("empty VDP scope requires an official source and no assets: " + ident)
        if item["status"] == "fetch_failed" and (item.get("assets") or not item.get("error")):
            raise Invalid("failed VDP scope requires an error and no assets: " + ident)
        captures[ident] = item
    return captures


def vdp_record(listing, capture):
    status = capture["status"] if capture else "not_attempted"
    assets = capture.get("assets", []) if capture and status == "captured" else []
    limitations = ["Only the published asset table was captured; program rules and submission eligibility still require individual review."]
    if status != "captured":
        limitations.append("No public asset rows were captured; consult the live official program policy for any policy-defined scope.")
    return {
        "id": listing["id"], "name": listing["name"], "program_url": listing["program_url"],
        "program_type": "vulnerability_disclosure", "directory_category": "vdp",
        "directory_card": listing.get("directory_card"),
        "scope_status": status, "scope_captured_at": capture["captured_at"] if capture else None,
        "scope_published_at": capture.get("published_at") if capture else None,
        "scope_group_count": capture.get("scope_groups") if capture else None,
        "capture_error": capture.get("error") if capture else None,
        "scope_source_urls": [capture["source_url"]] if capture and capture.get("source_url") else [],
        "in_scope": [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "in"],
        "out_of_scope": [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "out"],
        "policy_review_state": "scope_table_only" if status == "captured" else "directory_listing_only",
        "verified_policy_id": listing["verified_policy_id"],
        "visual_page": "docs/bugcrowd-programs/vdp/" + listing["id"] + ".md",
        "limitations": limitations,
    }


def bounty_record(listing, source, capture):
    return {
        "id": source["id"], "name": source["name"], "program_url": source["program_url"],
        "program_type": listing["program_type"], "directory_category": "bug_bounty",
        "directory_card": listing.get("directory_card"),
        "scope_status": source["scope_status"], "scope_captured_at": source["scope_captured_at"],
        "scope_published_at": capture.get("published_at") if capture else None,
        "scope_group_count": capture.get("scope_groups") if capture else None,
        "capture_error": capture.get("error") if capture else None,
        "scope_source_urls": source["scope_source_urls"],
        "in_scope": source["in_scope"], "out_of_scope": source["out_of_scope"],
        "policy_review_state": source["policy_review_state"],
        "verified_policy_id": source["verified_policy_id"],
        "visual_page": "docs/public-bounties/bugcrowd/" + source["id"] + ".md",
        "limitations": source["limitations"],
    }


def build(root=ROOT):
    discovery = json.loads(build_discovery(root)["exports/program-discovery.json"])
    batches = [batch for batch in discovery["batches"] if batch["platform"] == "Bugcrowd"]
    latest = max(batches, key=lambda batch: batch["reviewed_at"])
    snapshot_date = latest["reviewed_at"][:10]
    source_batch = json.loads((root / "data/program-discovery" / (latest["id"] + ".json")).read_text(encoding="utf-8"))
    current_ids = {item["id"] for item in source_batch["entries"]}
    current = {item["id"]: item for item in discovery["listings"]
               if item["platform"] == "Bugcrowd" and item["id"] in current_ids}
    if len(current) != len(source_batch["entries"]):
        raise Invalid("current Bugcrowd snapshot does not match deduplicated discovery identities")
    captures = load_vdp_captures(root, current, snapshot_date)
    bounty_catalog = json.loads(build_bounties(root)["exports/public-bounties.json"])
    bounty = {item["id"]: item for item in bounty_catalog["programs"]
              if item["platform"] == "Bugcrowd" and item["id"] in current}
    raw_bounty = {item["listing_id"]: item for item in json.loads(
        (root / "data/public-bounty-scopes.json").read_text(encoding="utf-8"))["captures"]
                  if item["platform"] == "Bugcrowd"}
    records = []
    for listing in current.values():
        if listing["program_type"] == "vulnerability_disclosure":
            records.append(vdp_record(listing, captures.get(listing["id"])))
        else:
            source = bounty.get(listing["id"])
            if source is None:
                raise Invalid("Bugcrowd bounty listing lacks a catalog record: " + listing["id"])
            records.append(bounty_record(listing, source, raw_bounty.get(listing["id"])))
    records.sort(key=lambda item: (item["directory_category"], item["name"].casefold(), item["id"]))
    by_status = dict(sorted(Counter(item["scope_status"] for item in records).items()))
    counts = {
        "current_public_programs": len(records),
        "bug_bounty_category": sum(item["directory_category"] == "bug_bounty" for item in records),
        "vulnerability_disclosure": sum(item["directory_category"] == "vdp" for item in records),
        "published_scope_captured": by_status.get("captured", 0),
        "scope_gaps": len(records) - by_status.get("captured", 0),
        "by_scope_status": by_status,
        "in_scope_entries": sum(len(item["in_scope"]) for item in records),
        "out_of_scope_entries": sum(len(item["out_of_scope"]) for item in records),
    }
    notice = ("Official public Bugcrowd directory and scope-table snapshots. A listing or asset row does not establish "
              "current testing permission, complete policy scope, report submission availability, or reward eligibility. "
              "Read the live program policy before research activity.")
    export = {"schema_version": "1.0.0", "directory_snapshot_date": snapshot_date,
              "directory_observed_at": latest["reviewed_at"], "directory_source_urls": [s["url"] for s in latest["sources"]],
              "notice": notice, "counts": counts, "programs": records}
    outputs = {"exports/bugcrowd-programs.json": json.dumps(export, ensure_ascii=False, indent=2) + "\n"}
    summary = ["# Public Bugcrowd program scopes", "",
               "[Library home](../README.md) · [Discovery queue](program-discovery.md) · [Public bounty catalog](public-bounties.md)",
               "", notice, "",
               f"**{counts['current_public_programs']} current visible public listings** in the {snapshot_date} directory snapshot: "
               f"{counts['bug_bounty_category']} Bug Bounty and {counts['vulnerability_disclosure']} Vulnerability Disclosure. "
               f"{counts['published_scope_captured']} have published scope rows captured; {counts['scope_gaps']} have explicit gaps. "
               f"The captured tables contain {counts['in_scope_entries']} in-scope and {counts['out_of_scope_entries']} out-of-scope rows.", "",
               "- " + link("Bug Bounty category", "bugcrowd-programs/bug-bounty.md") +
               " — paid status is unconfirmed where no monetary reward was displayed.",
               "- " + link("Vulnerability Disclosure category", "bugcrowd-programs/vdp.md") + ".", "",
               "## Scope gaps", "",
               "| Program | Category | Status |", "| --- | --- | --- |"]
    for item in records:
        if item["scope_status"] != "captured":
            target = item["visual_page"].removeprefix("docs/")
            summary.append("| " + link(item["name"], target) + " | " + text(item["directory_category"]) +
                           " | " + text(STATUS_LABELS[item["scope_status"]]) + " |")
    summary += ["", "[Machine-readable catalog](../exports/bugcrowd-programs.json) · "
                "[Dated directory evidence](program-discovery.md) · [Data policy](../DATA_POLICY.md)", ""]
    outputs["docs/bugcrowd-programs.md"] = "\n".join(summary)
    for category, title, filename in (("bug_bounty", "Bug Bounty", "bug-bounty.md"),
                                       ("vdp", "Vulnerability Disclosure", "vdp.md")):
        subset = [item for item in records if item["directory_category"] == category]
        lines = ["# Bugcrowd " + title + " public listings", "",
                 "[Bugcrowd overview](../bugcrowd-programs.md) · [Library home](../../README.md)", "",
                 notice, "", "| Program | Industry | Displayed reward | Scope status | In scope | Out of scope | Capture time |",
                 "| --- | --- | --- | --- | ---: | ---: | --- |"]
        for item in subset:
            target = ("../public-bounties/bugcrowd/" + item["id"] + ".md" if category == "bug_bounty"
                      else "vdp/" + item["id"] + ".md")
            card = item["directory_card"] or {}
            lines.append("| " + link(item["name"], target) + " | " + text(card.get("industry") or "—") +
                         " | " + text(card.get("reward_summary") or "—") + " | " + text(STATUS_LABELS[item["scope_status"]]) +
                         " | " + str(len(item["in_scope"])) + " | " + str(len(item["out_of_scope"])) +
                         " | " + text(item["scope_captured_at"] or "—") + " |")
            if category == "vdp":
                detail = ["# " + text(item["name"]), "",
                          "[VDP index](../vdp.md) · [Bugcrowd overview](../../bugcrowd-programs.md) · "
                          "[Discovery queue](../../program-discovery.md)", "", notice, "",
                          link("Official program", item["program_url"]), "",
                          "**Scope status:** " + STATUS_LABELS[item["scope_status"]] + ".", "",
                          "**Policy review:** " + text(item["policy_review_state"].replace("_", " ")) + ".", "",
                          "**Capture time:** " + text(item["scope_captured_at"] or "Not captured") + ".", ""]
                if item["directory_card"]:
                    detail += ["**Directory category:** " + text(card["publisher_category"]) + ".", "",
                               "**Industry:** " + text(card["industry"] or "Not listed") + ".", "",
                               "**Access label:** " + text(card["access_status"]) + ".", ""]
                if item["scope_source_urls"]:
                    detail += ["**Scope source:** " + ", ".join(link("Official source " + str(i), u)
                                                              for i, u in enumerate(item["scope_source_urls"], 1)), ""]
                detail += ["## In-scope entries (" + str(len(item["in_scope"])) + ")", ""]
                detail += render_asset_table(item["in_scope"])
                detail += ["## Out-of-scope entries (" + str(len(item["out_of_scope"])) + ")", ""]
                detail += render_asset_table(item["out_of_scope"])
                detail += ["**Limits**", ""] + ["- " + text(value) for value in item["limitations"]] + [""]
                outputs[item["visual_page"]] = "\n".join(detail)
        lines.append("")
        outputs["docs/bugcrowd-programs/" + filename] = "\n".join(lines)
    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for name, content in build().items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise SystemExit("Missing or stale Bugcrowd program output: " + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print("Current public Bugcrowd directory, scope coverage and deterministic outputs validated (offline).")


if __name__ == "__main__":
    main()
