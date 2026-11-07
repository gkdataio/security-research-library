"""Shared source exclusions for every public program/scope HTTP reader.

These are access restrictions, not evidence that a program closed or its scope
changed. Keep last-good records. There is deliberately no CLI override or expiry.
"""

import posixpath
from urllib.parse import unquote, urlsplit


EXCLUDED_BUGCROWD_ENGAGEMENTS = frozenset({"fmshrc-vdp", "abmc-vdp", "oshrc-vdp"})
EXCLUSION_REASON = "Source access excluded; no request made; current scope unknown; last-good data retained"


class SourceAccessExcluded(ValueError):
    """The source must not be requested through a different collection path."""


def excluded_source_reason(url):
    parts = urlsplit(url)
    if parts.hostname not in ("bugcrowd.com", "www.bugcrowd.com"):
        return None
    # Cover display aliases and every child (including saved brief JSON), not
    # only the engagement landing page. Match whole identities, never prefixes.
    path = posixpath.normpath(unquote(parts.path)).strip("/").split("/")
    if (len(path) >= 2 and path[0].lower() == "engagements"
            and path[1].lower() in EXCLUDED_BUGCROWD_ENGAGEMENTS):
        return EXCLUSION_REASON
    return None


def require_source_access(url):
    reason = excluded_source_reason(url)
    if reason:
        raise SourceAccessExcluded(reason)
