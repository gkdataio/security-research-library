#!/usr/bin/env python3
"""Validate dated public bounty scope captures and render a portable catalog."""

import argparse
from collections import Counter
import json
from urllib.parse import urlsplit

from build_navigation import link, text
from export_program_discovery import build as build_discovery
from scope_integrity import (SOURCE_METHODS, capture_source_kind, source_belongs_to_program,
                             validate_gap_review, validate_unique_scope_rows)
from validate import ROOT, Invalid, check_schema


PLATFORMS = ("Bugcrowd", "HackerOne", "Intigriti")
STATUS_LABELS = {
    "captured": "Published scope captured",
    "no_published_assets": "No published asset rows found",
    "preview_only": "Only a preview page was available",
    "terms_only": "Only public terms were available",
    "fetch_failed": "Scope fetch failed",
    "not_attempted": "Scope not yet fetched",
}


def load_captures(root, listings):
    path = root / "data/public-bounty-scopes.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads((root / "schema/public-bounty-scopes.schema.json").read_text(encoding="utf-8"))
    check_schema(data, schema, schema)
    by_id = {item["id"]: item for item in listings}
    captures = {}
    for item in data["captures"]:
        ident = item["listing_id"]
        if ident in captures:
            raise Invalid("duplicate public bounty capture ID: " + ident)
        listing = by_id.get(ident)
        if listing is None:
            raise Invalid("capture is not present in discovery queue: " + ident)
        if (any(item[field] != listing[field] for field in ("platform", "name", "program_url"))
                or item["directory_program_type"] != listing["program_type"]):
            raise Invalid("capture identity does not match discovery listing: " + ident)
        if item["platform"] not in PLATFORMS:
            raise Invalid("unsupported scope capture platform")
        source_url = item.get("source_url")
        status = item["status"]
        if source_url:
            if item.get("source_method") != SOURCE_METHODS[item["platform"]]:
                raise Invalid("scope capture method disagrees with platform: " + ident)
            kind = capture_source_kind(item["platform"], status)
            if not source_belongs_to_program(item["platform"], item["program_url"], source_url, kind):
                raise Invalid("scope source belongs to a different program: " + ident)
        elif item.get("source_method"):
            raise Invalid("scope capture method lacks a source URL: " + ident)
        assets = item.get("assets", [])
        validate_unique_scope_rows(assets, ident)
        validate_gap_review(item)
        if status == "captured" and (not assets or not source_url):
            raise Invalid("captured scope requires assets and official source: " + ident)
        if item.get("duplicate_source_rows") and status != "captured":
            raise Invalid("duplicate source row count requires a captured table: " + ident)
        if status in ("no_published_assets", "preview_only", "terms_only", "not_paid_bounty") and (assets or not source_url):
            raise Invalid("noncaptured scope must have an official source and no assets: " + ident)
        if status == "preview_only" and "/preview/" not in source_url:
            raise Invalid("preview-only status requires a preview source: " + ident)
        if status == "terms_only" and "/tac/" not in source_url:
            raise Invalid("terms-only status requires a terms source: " + ident)
        if status == "not_paid_bounty" and (item["platform"] != "HackerOne" or item.get("offers_bounties") is not False):
            raise Invalid("nonbounty classification requires HackerOne program evidence: " + ident)
        if item["platform"] == "HackerOne" and status != "fetch_failed":
            if item.get("offers_bounties") is not (status != "not_paid_bounty"):
                raise Invalid("HackerOne bounty flag disagrees with capture status: " + ident)
        if status == "fetch_failed" and not item.get("error"):
            raise Invalid("failed scope fetch requires an error: " + ident)
        if (item.get("published_asset_count") is not None
                and len(assets) + item.get("duplicate_source_rows", 0) != item["published_asset_count"]):
            raise Invalid("published asset count does not match captured rows: " + ident)
        captures[ident] = item
    return data, captures


def bounty_classification(listing, capture, verified):
    if verified and verified.get("program_type", {}).get("value") == "vulnerability_disclosure":
        return None
    if capture and capture["status"] == "not_paid_bounty":
        return None
    if verified and verified.get("program_type", {}).get("value") == "paid_bounty":
        return "verified_policy"
    if listing["platform"] == "HackerOne" and capture and capture.get("offers_bounties") is True:
        return "hackerone_program_flag"
    if listing["program_type"] == "paid_bounty":
        return "official_directory_paid_listing"
    if listing["platform"] == "Bugcrowd" and listing["program_type"] == "unknown":
        return "official_bounty_category_paid_unverified"
    return None


def catalog_record(listing, capture, verified, classification):
    if verified and verified.get("asset_scope"):
        scope = verified["asset_scope"]
        by_id = {source["id"]: source["url"] for source in verified["sources"]}
        source_urls = [by_id[key] for key in scope["source_ids"]]
        in_scope, out_of_scope = scope["in_scope"], scope["out_of_scope"]
        status = "captured"
        captured_at = scope["verified_at"]
        limitations = scope["limitations"]
        review_state = "verified_policy_record"
        duplicate_rows = 0
        gap_review = None
    else:
        status = capture["status"] if capture else "not_attempted"
        captured_at = capture["captured_at"] if capture else None
        source_urls = [capture["source_url"]] if capture and capture.get("source_url") else []
        assets = capture.get("assets", []) if capture and status == "captured" else []
        in_scope = [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "in"]
        out_of_scope = [{k: v for k, v in asset.items() if k != "scope"} for asset in assets if asset["scope"] == "out"]
        limitations = (["Only the published asset table was captured; program rules and eligibility still require individual review."]
                       if status == "captured" else ["Full program policy review remains outstanding."])
        duplicate_rows = capture.get("duplicate_source_rows", 0) if capture else 0
        gap_review = capture.get("gap_review") if capture else None
        if duplicate_rows:
            limitations.append(f"{duplicate_rows} repeated rows in the published table were collapsed in this catalog.")
        if any("█" in asset["name"] for asset in assets):
            limitations.append("The platform redacts at least one asset label; that row is not a usable target identifier.")
        if status != "captured":
            limitations.append("No complete public scope table is available in this capture; consult the live official program page.")
        if gap_review:
            limitations.append(gap_review["note"])
        review_state = "scope_table_only" if status == "captured" else "directory_listing_only"
    flags = []
    if "demo/test wording" in listing.get("evidence_note", ""):
        flags.append("Directory name contains demo/test wording; production-program identity needs review.")
    if "/dummy" in urlsplit(listing["program_url"]).path.lower():
        flags.append("Program URL contains a dummy path segment; production-program identity needs review.")
    if in_scope and all((asset.get("group") or "").casefold() == "no bounty" for asset in in_scope):
        flags.append("Every captured in-scope row is labeled No bounty by the platform.")
    if (listing["platform"] == "HackerOne" and in_scope
            and all(asset.get("bounty_eligible") is False for asset in in_scope)):
        flags.append("No captured in-scope row is marked bounty eligible by HackerOne.")
    return {
        "id": listing["id"], "name": listing["name"], "platform": listing["platform"],
        "program_url": listing["program_url"], "bounty_classification": classification,
        "directory_card": listing.get("directory_card"),
        "scope_source_duplicate_rows": duplicate_rows, "gap_review": gap_review,
        "policy_review_state": review_state, "verified_policy_id": listing["verified_policy_id"],
        "scope_status": status, "scope_captured_at": captured_at,
        "scope_source_urls": source_urls, "in_scope": in_scope, "out_of_scope": out_of_scope,
        "limitations": limitations, "review_flags": flags,
    }


def render_asset_table(assets):
    if not assets:
        return ["No explicit asset rows were captured in this category. The policy may still impose exclusions.", ""]
    lines = ["| Asset | Type | Location | Group | Qualification |",
             "| --- | --- | --- | --- | --- |"]
    for asset in assets:
        qualification = asset.get("note", "")
        if "bounty_eligible" in asset:
            qualifier = "Bounty eligible" if asset["bounty_eligible"] else "Not bounty eligible"
            qualification = (qualification + "; " if qualification else "") + qualifier
        lines.append("| " + text(asset["name"]) + " | " + text(asset["asset_type"]) + " | " +
                     text(asset.get("location") or "—") + " | " + text(asset.get("group") or "—") +
                     " | " + text(qualification or "—") + " |")
    return lines + [""]


def build(root=ROOT):
    discovery = json.loads(build_discovery(root)["exports/program-discovery.json"])
    listings = [item for item in discovery["listings"] if item["platform"] in PLATFORMS]
    capture_data, captures = load_captures(root, listings)
    directory_date = max(batch["reviewed_at"][:10] for batch in discovery["batches"])
    if capture_data["directory_snapshot_date"] != directory_date:
        raise Invalid("scope captures must identify the matching directory snapshot date")
    verified = {record["id"]: record for path in (root / "data/programs").glob("*.json")
                for record in [json.loads(path.read_text(encoding="utf-8"))]}
    records = []
    for listing in listings:
        capture = captures.get(listing["id"])
        policy = verified.get(listing["verified_policy_id"])
        classification = bounty_classification(listing, capture, policy)
        if classification:
            records.append(catalog_record(listing, capture, policy, classification))
    records.sort(key=lambda item: (item["platform"], item["name"].casefold(), item["id"]))
    counts = {
        "observed_bounty_candidates": len(records),
        "with_published_scope": sum(item["scope_status"] == "captured" for item in records),
        "scope_not_captured": sum(item["scope_status"] != "captured" for item in records),
        "verified_policy_records": sum(item["policy_review_state"] == "verified_policy_record" for item in records),
        "scope_table_only": sum(item["policy_review_state"] == "scope_table_only" for item in records),
        "with_review_flags": sum(bool(item["review_flags"]) for item in records),
        "in_scope_entries": sum(len(item["in_scope"]) for item in records),
        "out_of_scope_entries": sum(len(item["out_of_scope"]) for item in records),
        "duplicate_source_rows_removed": sum(item["scope_source_duplicate_rows"] for item in records),
        "hackerone_nonbounty_flags": sum(item["platform"] == "HackerOne" and item["status"] == "not_paid_bounty" for item in captures.values()),
        "unconfirmed_bugcrowd_bounty_category": sum(item["bounty_classification"] == "official_bounty_category_paid_unverified" for item in records),
        "unclassified_queue_listings": sum(item["program_type"] == "unknown" and item["id"] not in captures
                                           and item["verified_policy_id"] is None
                                           for item in listings),
        "by_platform": {platform: sum(item["platform"] == platform for item in records) for platform in PLATFORMS},
        "by_scope_status": dict(sorted(Counter(item["scope_status"] for item in records).items())),
    }
    notice = ("Dated official directory and scope-table snapshots for publicly listed bounties. "
              "A listing or asset row alone does not establish current authorization, bounty eligibility, or complete policy scope. "
              "Read the live program policy before any activity.")
    export = {"schema_version": "1.0.0", "directory_snapshot_date": directory_date,
              "notice": notice, "counts": counts, "programs": records}
    lines = ["# Public bounty scope catalog", "",
             "[Library home](../README.md) · [Verified program policies](programs.md) · [Discovery queue](program-discovery.md)",
             "", notice, "",
             f"**{counts['observed_bounty_candidates']} observed bounty candidates** across Bugcrowd, HackerOne, and Intigriti. "
             f"{counts['with_published_scope']} have captured scope rows; {counts['scope_not_captured']} do not. "
             f"{counts['verified_policy_records']} have separately reviewed policy records. "
             f"{counts['unconfirmed_bugcrowd_bounty_category']} Bugcrowd category listings have unconfirmed paid status. "
             "Counts reflect the dated directory snapshot, not every bounty that may exist today.", "",
             "| Platform | Bounty candidates | Scope captured |", "| --- | ---: | ---: |"]
    outputs = {"exports/public-bounties.json": json.dumps(export, indent=2, ensure_ascii=False) + "\n"}
    for platform in PLATFORMS:
        subset = [item for item in records if item["platform"] == platform]
        lines.append("| " + link(platform, "public-bounties/" + platform.lower() + ".md") + " | " +
                     str(len(subset)) + " | " + str(sum(item["scope_status"] == "captured" for item in subset)) + " |")
        page = ["# " + platform + " public bounty scopes", "",
                "[Bounty overview](../public-bounties.md) · [Verified policies](../programs.md) · [Discovery queue](../program-discovery.md)",
                "", notice, "",
                "| Program | Scope status | In scope | Out of scope | Review flags | Capture time |",
                "| --- | --- | ---: | ---: | ---: | --- |"]
        for item in subset:
            page.append("| " + link(item["name"], platform.lower() + "/" + item["id"] + ".md") + " | " +
                        text(STATUS_LABELS[item["scope_status"]]) + " | " +
                        str(len(item["in_scope"])) + " | " + str(len(item["out_of_scope"])) + " | " +
                        str(len(item["review_flags"])) + " | " +
                        text(item["scope_captured_at"] or "—") + " |")
            detail = ["# " + text(item["name"].strip()), "",
                      "[" + platform + " bounty index](../" + platform.lower() + ".md) · " +
                      "[Bounty overview](../../public-bounties.md) · [Discovery queue](../../program-discovery.md)", "",
                      notice, "",
                      link("Official program", item["program_url"]) +
                      (" · " + link("Reviewed policy and JSON", "../../programs.md#program-" + item["verified_policy_id"])
                       if item["verified_policy_id"] else ""), "",
                      "**Scope status:** " + STATUS_LABELS[item["scope_status"]] + ".", "",
                      "**Policy review:** " + text(item["policy_review_state"].replace("_", " ")) + ".", "",
                      "**Capture time:** " + text(item["scope_captured_at"] or "Not captured") + ".", ""]
            if item["directory_card"]:
                card = item["directory_card"]
                detail += ["**Directory category:** " + text(card["publisher_category"]) + ".", "",
                           "**Displayed reward:** " + text(card["reward_summary"] or "Not displayed") + ".", "",
                           "**Industry:** " + text(card["industry"] or "Not listed") + ".", ""]
            if item["scope_source_urls"]:
                detail += ["**Scope source:** " + ", ".join(link("Official source " + str(i), url)
                                                        for i, url in enumerate(item["scope_source_urls"], 1)), ""]
            detail += ["## In-scope entries (" + str(len(item["in_scope"])) + ")", ""]
            detail += render_asset_table(item["in_scope"])
            detail += ["## Out-of-scope entries (" + str(len(item["out_of_scope"])) + ")", ""]
            detail += render_asset_table(item["out_of_scope"])
            detail += ["**Limits**", ""] + ["- " + text(value) for value in item["limitations"]] + [""]
            if item["review_flags"]:
                detail += ["**Review flags**", ""] + ["- " + text(value) for value in item["review_flags"]] + [""]
            outputs["docs/public-bounties/" + platform.lower() + "/" + item["id"] + ".md"] = "\n".join(detail)
        page.append("")
        outputs["docs/public-bounties/" + platform.lower() + ".md"] = "\n".join(page)
    lines += ["", "## Scope gaps", "",
              "These candidates need an accessible official scope table or individual policy review before their asset coverage can be represented here.", "",
              "| Program | Platform | Capture status |", "| --- | --- | --- |"]
    for item in records:
        if item["scope_status"] != "captured":
            target = "public-bounties/" + item["platform"].lower() + "/" + item["id"] + ".md"
            lines.append("| " + link(item["name"], target) + " | " + text(item["platform"]) +
                         " | " + text(STATUS_LABELS[item["scope_status"]]) + " |")
    lines += ["", "The [machine-readable export](../exports/public-bounties.json) records each candidate's classification evidence, capture status, source links and asset rows. "
              "Programs with inaccessible or unpublished scope remain visible with their capture status.", ""]
    outputs["docs/public-bounties.md"] = "\n".join(lines)
    return outputs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for name, content in build().items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                raise SystemExit("Missing or stale public bounty output: " + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print("Public bounty scope captures and deterministic outputs validated (offline).")


if __name__ == "__main__":
    main()
