#!/usr/bin/env python3
"""Compare stored programs and optionally watch their official public pages.

The live mode makes read-only GET requests to recorded program/policy pages and
scope-source URLs. It never requests an asset named by an in-scope row. A changed
response is a review lead, not a verified policy or scope change.
"""

import argparse
from collections import Counter, defaultdict
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from export_bugcrowd_programs import build as build_bugcrowd
from export_program_discovery import build as build_discovery
from export_programs import build as build_programs
from export_public_bounties import build as build_bounties
from validate import ROOT, Invalid


EXPORT_PATHS = {
    "discovery": "exports/program-discovery.json",
    "programs": "exports/programs.json",
    "bounties": "exports/public-bounties.json",
    "bugcrowd": "exports/bugcrowd-programs.json",
    "bounty_captures": "data/public-bounty-scopes.json",
    "vdp_captures": "data/bugcrowd-vdp-scopes.json",
}
DEFAULT_STATE = ROOT / ".program-change-state.json"


def _load_current(root):
    built = {
        "discovery": build_discovery(root),
        "programs": build_programs(root),
        "bounties": build_bounties(root),
        "bugcrowd": build_bugcrowd(root),
    }
    result = {name: json.loads(built[name][path]) for name, path in EXPORT_PATHS.items()
              if name in built}
    for name in ("bounty_captures", "vdp_captures"):
        result[name] = json.loads((root / EXPORT_PATHS[name]).read_text(encoding="utf-8"))
    return result


def _load_ref(root, ref):
    commit = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "--end-of-options",
                             ref + "^{commit}"],
                            capture_output=True, text=True, check=False)
    if commit.returncode:
        raise Invalid("unknown Git baseline: " + ref)
    sha = commit.stdout.strip()
    result = {}
    for name, path in EXPORT_PATHS.items():
        found = subprocess.run(["git", "-C", str(root), "show", sha + ":" + path],
                               capture_output=True, check=False)
        if found.returncode:
            raise Invalid("baseline lacks " + path + "; choose a newer commit")
        result[name] = json.loads(found.stdout.decode("utf-8"))
    return sha, result


def _without_evidence_ids(value):
    if value is None:
        return None
    return {key: item for key, item in value.items() if key not in ("source_ids", "verified_at")}


def _scope_rows(rows):
    normalized = [{key: value for key, value in row.items() if key != "source_ids"} for row in rows]
    unique = {json.dumps(row, sort_keys=True, ensure_ascii=False): row for row in normalized}
    return [unique[key] for key in sorted(unique)]


def _policy_view(policy):
    scope = policy.get("asset_scope") or {}
    context = policy.get("scope_context")
    return {
        "name": policy["name"], "operator": policy["operator"], "platform": policy["platform"],
        "program_url": policy["program_url"], "policy_url": policy["policy_url"],
        "announcement_urls": policy["announcement_urls"], "change_log_url": policy["change_log_url"],
        "program_type": _without_evidence_ids(policy.get("program_type")),
        "submission_status": _without_evidence_ids(policy.get("submission_status")),
        "rewards": _without_evidence_ids(policy["rewards"]),
        "eligibility": _without_evidence_ids(policy["eligibility"]),
        "restrictions": _without_evidence_ids(policy["restrictions"]),
        "scope_context": _without_evidence_ids(context),
        "asset_scope": ({"capture_status": scope.get("capture_status"),
                         "collection_method": scope.get("collection_method"),
                         "in_scope": _scope_rows(scope.get("in_scope", [])),
                         "out_of_scope": _scope_rows(scope.get("out_of_scope", [])),
                         "limitations": scope.get("limitations", [])} if scope else None),
    }


def _listing_view(listing, latest_batch_ids):
    view = {key: listing.get(key) for key in (
        "name", "platform", "program_url", "program_type", "submission_status", "directory_card",
        "evidence_note", "verified_policy_id")}
    current = latest_batch_ids.get(listing["platform"])
    view["observed_in_latest_directory_batch"] = (
        any(obs["batch_id"] in current for obs in listing["observations"]) if current else None)
    return view


def _capture_view(capture):
    if capture is None:
        return None
    assets = capture.get("assets", [])
    return {
        "status": capture["status"], "source_url": capture.get("source_url"),
        "offers_bounties": capture.get("offers_bounties"),
        "published_at": capture.get("published_at"),
        "scope_groups": capture.get("scope_groups"),
        "in_scope": _scope_rows([row for row in assets if row["scope"] == "in"]),
        "out_of_scope": _scope_rows([row for row in assets if row["scope"] == "out"]),
    }


def inventory(payload):
    """Keep each directory identity once, attaching its reviewed policy if any."""
    policies = {item["id"]: item for item in payload["programs"]["programs"]}
    bounty = {item["listing_id"]: item for item in payload["bounty_captures"]["captures"]}
    vdp = {item["listing_id"]: item for item in payload["vdp_captures"]["captures"]}
    if len(bounty) != len(payload["bounty_captures"]["captures"]) or len(vdp) != len(payload["vdp_captures"]["captures"]):
        raise Invalid("duplicate canonical scope capture ID")
    if set(bounty) & set(vdp):
        raise Invalid("same listing appears in both scope capture files")
    latest_at = {}
    latest_batch_ids = defaultdict(set)
    for batch in payload["discovery"].get("batches", []):
        platform = batch["platform"]
        if batch["reviewed_at"] > latest_at.get(platform, ""):
            latest_at[platform] = batch["reviewed_at"]
            latest_batch_ids[platform] = {batch["id"]}
        elif batch["reviewed_at"] == latest_at[platform]:
            latest_batch_ids[platform].add(batch["id"])
    records = {}
    attached = set()
    for listing in payload["discovery"]["listings"]:
        key = "listing:" + listing["id"]
        policy_id = listing["verified_policy_id"]
        if policy_id:
            if policy_id not in policies:
                raise Invalid("discovery links missing reviewed policy: " + policy_id)
            attached.add(policy_id)
        records[key] = {
            "name": listing["name"], "platform": listing["platform"],
            "program_url": listing["program_url"], "listing": _listing_view(listing, latest_batch_ids),
            "policy": _policy_view(policies[policy_id]) if policy_id else None,
            "capture": _capture_view(bounty.get(listing["id"]) or vdp.get(listing["id"])),
        }
    if len(records) != len(payload["discovery"]["listings"]):
        raise Invalid("duplicate discovery listing ID")
    for policy_id, policy in policies.items():
        if policy_id not in attached:
            records["policy:" + policy_id] = {
                "name": policy["name"], "platform": policy["platform"],
                "program_url": policy["program_url"], "listing": None,
                "policy": _policy_view(policy), "capture": None,
            }
    return records


def _field_changes(before, after, path=""):
    changes = []
    if isinstance(before, dict) and isinstance(after, dict):
        for key in sorted(set(before) | set(after)):
            changes.extend(_field_changes(before.get(key), after.get(key), path + "." + key if path else key))
    elif before != after:
        if path.endswith(".in_scope") or path.endswith(".out_of_scope"):
            old = {json.dumps(row, sort_keys=True, ensure_ascii=False) for row in (before or [])}
            new = {json.dumps(row, sort_keys=True, ensure_ascii=False) for row in (after or [])}
            changes.append({"field": path, "removed": [json.loads(row) for row in sorted(old - new)],
                            "added": [json.loads(row) for row in sorted(new - old)]})
        else:
            changes.append({"field": path, "before": before, "after": after})
    return changes


def compare_inventories(before, after):
    changes = []
    for key in sorted(set(before) | set(after)):
        old, new = before.get(key), after.get(key)
        if old is None or new is None:
            item = new or old
            changes.append({"key": key, "name": item["name"], "platform": item["platform"],
                            "program_url": item["program_url"],
                            "kind": "added" if old is None else "removed", "fields": []})
            continue
        fields = _field_changes({k: v for k, v in old.items() if k not in ("name", "platform", "program_url")},
                                {k: v for k, v in new.items() if k not in ("name", "platform", "program_url")})
        for field in ("name", "platform", "program_url"):
            if old[field] != new[field]:
                fields.insert(0, {"field": field, "before": old[field], "after": new[field]})
        if fields:
            changes.append({"key": key, "name": new["name"], "platform": new["platform"],
                            "program_url": new["program_url"], "kind": "changed", "fields": fields})
    return changes


def official_targets(payload, include_scope_sources=True):
    """Build a request list solely from recorded official program/policy URLs."""
    targets = defaultdict(lambda: {"programs": set(), "roles": set(), "platforms": set()})

    def add(url, program, platform, role):
        if not url:
            return
        parts = urlsplit(url)
        if (parts.scheme != "https" or not parts.hostname or parts.username or parts.password
                or parts.port or parts.fragment):
            raise Invalid("unsafe official page URL in stored program: " + program)
        item = targets[url]
        item["programs"].add(program)
        item["roles"].add(role)
        item["platforms"].add(platform)

    for listing in payload["discovery"]["listings"]:
        add(listing["program_url"], "listing:" + listing["id"], listing["platform"], "program_page")
    for policy in payload["programs"]["programs"]:
        key = "policy:" + policy["id"]
        add(policy["program_url"], key, policy["platform"], "program_page")
        add(policy["policy_url"], key, policy["platform"], "policy_page")
        if include_scope_sources and policy.get("asset_scope"):
            by_id = {source["id"]: source["url"] for source in policy["sources"]}
            for source_id in policy["asset_scope"]["source_ids"]:
                add(by_id[source_id], key, policy["platform"], "scope_source")
    if include_scope_sources:
        for filename in ("bounty_captures", "vdp_captures"):
            for capture in payload[filename]["captures"]:
                add(capture.get("source_url"), "listing:" + capture["listing_id"],
                    capture["platform"], "scope_source")
    return {url: {key: sorted(value) for key, value in item.items()}
            for url, item in sorted(targets.items())}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def _safe_redirect(base, location):
    if not location:
        return None
    parts = urlsplit(urljoin(base, location))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def fetch_official_page(url, prior=None, timeout=15, max_bytes=2_000_000, opener=None):
    headers = {"User-Agent": "security-research-library-program-change-check/1.0",
               "Accept": "text/html, application/json;q=0.9, text/plain;q=0.8",
               "Accept-Encoding": "identity"}
    if prior and prior.get("etag") and "\n" not in prior["etag"] and "\r" not in prior["etag"]:
        headers["If-None-Match"] = prior["etag"]
    elif prior and prior.get("last_modified") and "\n" not in prior["last_modified"] and "\r" not in prior["last_modified"]:
        headers["If-Modified-Since"] = prior["last_modified"]
    opener = opener or build_opener(NoRedirect())
    try:
        response = opener.open(Request(url, headers=headers, method="GET"), timeout=timeout)
    except HTTPError as error:
        response = error
    except (URLError, TimeoutError, OSError) as error:
        return {"kind": "unavailable", "reason": type(error).__name__}
    with response:
        status = response.code
        if status == 304 and prior:
            return {"kind": "not_modified"}
        if status in (401, 403, 429) or status >= 500:
            return {"kind": "unavailable", "status": status,
                    "reason": "rate_limited" if status == 429 else "access_or_server_error"}
        etag = response.headers.get("ETag")
        modified = response.headers.get("Last-Modified")
        if 300 <= status < 400:
            fingerprint = {"status": status, "redirect_to": _safe_redirect(
                url, response.headers.get("Location"))}
        elif status == 404 or status == 410:
            fingerprint = {"status": status}
        elif status in (200, 204):
            content_type = response.headers.get("Content-Type", "").split(";", 1)[0].lower().strip()
            if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                return {"kind": "unavailable", "status": status, "reason": "unexpected_content_encoding"}
            if content_type not in ("text/html", "text/plain", "application/json", "application/ld+json",
                                    "application/xhtml+xml"):
                return {"kind": "unavailable", "status": status, "reason": "unsupported_content_type"}
            body = response.read(max_bytes + 1)
            if len(body) > max_bytes:
                return {"kind": "unavailable", "status": status, "reason": "response_too_large"}
            fingerprint = {"status": status, "content_type": content_type,
                           "sha256": hashlib.sha256(body).hexdigest()}
        else:
            return {"kind": "unavailable", "status": status, "reason": "unexpected_status"}
        return {"kind": "observed", "fingerprint": fingerprint,
                "etag": etag, "last_modified": modified}


def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _read_state(path):
    if not path.is_file():
        return {"schema_version": "1.0.0", "pages": {}}
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("schema_version") != "1.0.0" or not isinstance(state.get("pages"), dict):
        raise Invalid("unsupported local program-change state file")
    return state


def _write_json_atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent,
                                     prefix=path.name + ".", suffix=".tmp", delete=False) as handle:
        temp = Path(handle.name)
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    os.replace(temp, path)


def _recent(entry, hours, now):
    if not entry or hours <= 0:
        return False
    try:
        times = [dt.datetime.fromisoformat(entry[field].replace("Z", "+00:00"))
                 for field in ("checked_at", "attempted_at") if entry.get(field)]
    except ValueError:
        return False
    if not times:
        return False
    age = now - max(times)
    return dt.timedelta(0) <= age < dt.timedelta(hours=hours)


def check_live(targets, state_path, *, plan=False, max_requests=None, interval=1.0,
               timeout=15, max_bytes=2_000_000, skip_recent_hours=12,
               platforms=None, programs=None, fetcher=fetch_official_page):
    state = _read_state(state_path)
    now = dt.datetime.now(dt.timezone.utc)
    selected = {url: item for url, item in targets.items()
                if (not platforms or set(item["platforms"]) & set(platforms))
                and (not programs or set(item["programs"]) & set(programs)
                     or any(program.rsplit(":", 1)[-1] in programs for program in item["programs"]))}
    results = []
    counts = Counter()
    requests = 0
    scheduled = 0
    last_request = None
    for url, item in selected.items():
        prior = state["pages"].get(url)
        if _recent(prior, skip_recent_hours, now):
            counts["skipped_unavailable" if prior.get("last_failure") else "skipped_recent"] += 1
            continue
        if max_requests is not None and scheduled >= max_requests:
            counts["deferred"] += 1
            continue
        scheduled += 1
        if plan:
            counts["planned"] += 1
            continue
        if last_request is not None:
            time.sleep(max(0, interval - (time.monotonic() - last_request)))
        last_request = time.monotonic()
        requests += 1
        observed = fetcher(url, prior, timeout=timeout, max_bytes=max_bytes)
        kind = observed["kind"]
        if kind == "unavailable":
            counts["unavailable"] += 1
            results.append({"url": url, **item, "kind": kind, "status": observed.get("status"),
                            "reason": observed["reason"]})
            if observed.get("reason") == "rate_limited":
                counts["rate_limited"] += 1
                break
            state["pages"][url] = {**(prior or {}), "attempted_at": _now(),
                                   "last_failure": {"status": observed.get("status"),
                                                    "reason": observed["reason"]}}
            _write_json_atomic(state_path, state)
            continue
        if kind == "not_modified":
            counts["unchanged"] += 1
            prior["checked_at"] = _now()
            prior.pop("last_failure", None)
        else:
            fingerprint = observed["fingerprint"]
            old = prior.get("fingerprint") if prior else None
            kind = "baselined" if old is None else "unchanged" if old == fingerprint else "changed"
            counts[kind] += 1
            if kind == "changed":
                results.append({"url": url, **item, "kind": kind,
                                "before": old, "after": fingerprint})
            state["pages"][url] = {"fingerprint": fingerprint, "etag": observed.get("etag"),
                                   "last_modified": observed.get("last_modified"), "checked_at": _now()}
        _write_json_atomic(state_path, state)
    counts["total_targets"] = len(targets)
    counts["selected_targets"] = len(selected)
    counts["requests"] = requests
    if counts["rate_limited"]:
        counts["deferred"] += len(selected) - sum(counts[k] for k in (
            "skipped_recent", "skipped_unavailable", "unavailable", "unchanged", "changed",
            "baselined", "deferred"))
    return {"mode": "plan" if plan else "live", "state_file": str(state_path),
            "counts": dict(sorted(counts.items())), "signals": results,
            "notice": "A changed HTTP response is a review lead, not a verified program, scope or eligibility change."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="HEAD", help="Git commit used for saved-data comparison (default: HEAD)")
    parser.add_argument("--live", action="store_true", help="Check recorded official pages over HTTPS")
    parser.add_argument("--plan", action="store_true", help="Show live request coverage without making requests")
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE,
                        help="Local HTTP fingerprint state; ignored by Git by default")
    parser.add_argument("--max-requests", type=int, help="Maximum HTTP requests in this run")
    parser.add_argument("--interval", type=float, default=1.0, help="Minimum seconds between HTTP requests")
    parser.add_argument("--timeout", type=float, default=15.0, help="Per-request timeout in seconds")
    parser.add_argument("--max-bytes", type=int, default=2_000_000, help="Maximum bytes read from a response")
    parser.add_argument("--skip-recent-hours", type=float, default=12.0,
                        help="Skip URLs checked successfully within this many hours; use 0 to recheck")
    parser.add_argument("--pages-only", action="store_true", help="Skip official scope-source URLs in live mode")
    parser.add_argument("--platform", action="append", choices=("Bugcrowd", "HackerOne", "Intigriti",
                                                                  "Independent", "Direct vendor program",
                                                                  "HackerOne submission channel", "MSRC", "Bugzilla"))
    parser.add_argument("--program", action="append", help="Only check this listing:<id> or policy:<id> in live mode")
    parser.add_argument("--json-out", type=Path, help="Write a machine-readable report")
    parser.add_argument("--fail-on-change", action="store_true", help="Exit 1 when a saved or live change is found")
    args = parser.parse_args()
    if args.plan and not args.live:
        parser.error("--plan requires --live")
    if args.json_out and args.live and args.json_out.resolve() == args.state.resolve():
        parser.error("--json-out must differ from the local --state file")
    if (args.max_requests is not None and args.max_requests < 0 or args.interval < 0
            or args.timeout <= 0 or args.max_bytes <= 0 or args.skip_recent_hours < 0):
        parser.error("request limits and intervals must be nonnegative; timeout and bytes must be positive")
    current = _load_current(ROOT)
    baseline_sha, baseline = _load_ref(ROOT, args.base)
    before, after = inventory(baseline), inventory(current)
    saved_changes = compare_inventories(before, after)
    report = {"checked_at": _now(), "baseline_commit": baseline_sha,
              "saved_data": {"baseline_programs": len(before), "current_programs": len(after),
                             "changed_programs": len(saved_changes), "changes": saved_changes,
                             "notice": "Saved-data differences show semantic program fields, not review timestamps or repeated-row cleanup."}}
    print(f"Saved programs: {len(after)} current, {len(saved_changes)} changed against {args.base}.")
    for item in saved_changes[:20]:
        fields = ", ".join(field["field"] for field in item["fields"])
        print(f"  {item['kind']}: {item['name']} [{item['platform']}]" +
              (f" — {fields}" if fields else ""))
    if len(saved_changes) > 20:
        print(f"  ... {len(saved_changes) - 20} more; use --json-out for every change.")
    if args.live:
        targets = official_targets(current, include_scope_sources=not args.pages_only)
        live = check_live(targets, args.state, plan=args.plan, max_requests=args.max_requests,
                          interval=args.interval, timeout=args.timeout, max_bytes=args.max_bytes,
                          skip_recent_hours=args.skip_recent_hours, platforms=args.platform,
                          programs=args.program)
        report["official_pages"] = live
        print("Official pages: " + ", ".join(f"{key}={value}" for key, value in live["counts"].items()))
        changed_pages = [signal for signal in live["signals"] if signal["kind"] == "changed"]
        for signal in changed_pages[:20]:
            print("  review page: " + signal["url"] + " (" + ", ".join(signal["programs"]) + ")")
        if len(changed_pages) > 20:
            print(f"  ... {len(changed_pages) - 20} more changed pages; use --json-out.")
    if args.json_out:
        _write_json_atomic(args.json_out, report)
        print("Report: " + str(args.json_out))
    if args.fail_on_change and (saved_changes or report.get("official_pages", {}).get("counts", {}).get("changed", 0)):
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except Invalid as error:
        raise SystemExit("Program change check failed: " + str(error)) from None
