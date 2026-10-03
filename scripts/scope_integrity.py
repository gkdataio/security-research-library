"""Shared offline checks for sourced scope rows and program-specific URLs."""

import datetime as dt
import re
from urllib.parse import urlsplit

from validate import Invalid


SOURCE_METHODS = {
    "Bugcrowd": "public_bugcrowd_scope_groups",
    "HackerOne": "public_hackerone_program_and_structured_scopes",
    "Intigriti": "public_intigriti_asset_table",
}


def _fold(value):
    return value.strip().casefold() if isinstance(value, str) else value


def scope_row_key(row, scope=None):
    """Preserve scope, qualification and eligibility when finding repeated rows."""
    return (
        scope if scope is not None else row.get("scope"),
        _fold(row["name"]), _fold(row["asset_type"]),
        _fold(row.get("location") or ""), _fold(row.get("group") or ""),
        ("bounty_eligible" in row, row.get("bounty_eligible")),
        _fold(row.get("note")),
    )


def validate_unique_scope_rows(rows, program_id, scope=None):
    seen = set()
    for row in rows:
        key = scope_row_key(row, scope)
        if key in seen:
            raise Invalid("duplicate scope row in " + program_id)
        seen.add(key)


def _host(platform, hostname):
    if platform == "Bugcrowd":
        return "bugcrowd.com" if hostname in ("bugcrowd.com", "www.bugcrowd.com") else hostname
    if platform == "HackerOne":
        return "hackerone.com" if hostname in ("hackerone.com", "www.hackerone.com") else hostname
    return hostname


def capture_source_kind(platform, status):
    if platform == "Bugcrowd":
        return "bugcrowd_scope"
    if platform == "HackerOne":
        return "hackerone_program" if status == "not_paid_bounty" else "hackerone_scope"
    if platform == "Intigriti":
        return {"preview_only": "intigriti_preview", "terms_only": "intigriti_terms"}.get(
            status, "intigriti_detail")
    raise Invalid("unsupported scope platform: " + platform)


def source_belongs_to_program(platform, program_url, source_url, kind):
    """Bind an official platform scope URL to the exact program path.

    HackerOne's directory-only ``?type=team`` and root/www host aliases are
    display/canonical URL variants. They do not change the program handle.
    """
    program, source = urlsplit(program_url), urlsplit(source_url)
    try:
        nondefault_port = bool(program.port or source.port)
    except ValueError:
        return False
    if (program.scheme != "https" or source.scheme != "https" or source.query or source.fragment
            or program.username or program.password or source.username or source.password
            or nondefault_port or _host(platform, program.hostname) != _host(platform, source.hostname)):
        return False
    path = program.path.rstrip("/")
    source_path = source.path.rstrip("/")
    if platform == "Bugcrowd" and kind == "bugcrowd_scope":
        if program.hostname not in ("bugcrowd.com", "www.bugcrowd.com", "eu.bugcrowd.net", "gov.bugcrowd.net"):
            return False
        return bool(re.fullmatch(re.escape(path) + r"/changelog/[^/]+\.json", source_path))
    if platform == "HackerOne" and kind in ("hackerone_program", "hackerone_scope"):
        if _host(platform, program.hostname) != "hackerone.com" or not re.fullmatch(r"/[A-Za-z0-9_-]+", path):
            return False
        expected = path if kind == "hackerone_program" else path + "/policy_scopes"
        return source_path == expected
    if platform == "Intigriti" and kind in ("intigriti_detail", "intigriti_preview", "intigriti_terms"):
        if program.hostname != "app.intigriti.com" or not re.fullmatch(r"/programs/[^/]+/[^/]+", path):
            return False
        suffix = {"intigriti_detail": "/detail", "intigriti_preview": "/preview/detail",
                  "intigriti_terms": "/tac/detail"}[kind]
        return source_path == path + suffix
    return False


def validate_gap_review(item):
    review = item.get("gap_review")
    if review is None:
        return
    status = item["status"]
    expected = {
        "fetch_failed": {"http_403"},
        "no_published_assets": {"empty_published_table", "javascript_required"},
        "preview_only": {"preview_login_gate"},
        "terms_only": {"terms_login_gate"},
    }
    if review["result"] not in expected.get(status, set()):
        raise Invalid("gap review result conflicts with scope status: " + item["listing_id"])
    if review["policy_url"] not in {item["program_url"], item.get("source_url")}:
        raise Invalid("gap review URL is not this program policy: " + item["listing_id"])
    captured = dt.datetime.fromisoformat(item["captured_at"].replace("Z", "+00:00"))
    reviewed = dt.datetime.fromisoformat(review["reviewed_at"].replace("Z", "+00:00"))
    if reviewed < captured:
        raise Invalid("gap review predates scope capture: " + item["listing_id"])
    if review["result"] == "http_403" and review["http_status"] != 403:
        raise Invalid("HTTP 403 gap lacks matching response status: " + item["listing_id"])
    if review["result"] != "http_403" and review["http_status"] != 200:
        raise Invalid("public policy gap lacks HTTP 200 response: " + item["listing_id"])
