#!/usr/bin/env python3
"""Validate the basic shape of a MATT SEO Agent site config."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL_FIELDS = {
    "site_name": str,
    "domain": str,
    "cms": str,
    "primary_audience": str,
    "business_goal": str,
    "markets": list,
    "topics": list,
    "competitors": list,
    "conversion_events": list,
    "publishing_constraints": dict,
    "integrations": dict,
}


def fail(message: str) -> None:
    print(f"Config invalid: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate(path: Path) -> None:
    if not path.exists():
        fail(f"{path} does not exist")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")

    for field, expected_type in REQUIRED_TOP_LEVEL_FIELDS.items():
        if field not in data:
            fail(f"missing required field: {field}")
        if not isinstance(data[field], expected_type):
            fail(f"{field} must be {expected_type.__name__}")

    domain = data["domain"]
    if not domain.startswith(("https://", "http://")):
        fail("domain must start with http:// or https://")

    if not data["markets"]:
        fail("markets must contain at least one market")

    for index, market in enumerate(data["markets"]):
        if not isinstance(market, dict):
            fail(f"markets[{index}] must be an object")
        for field in ("country", "language", "location_code", "language_code"):
            if field not in market:
                fail(f"markets[{index}] missing {field}")

    integrations = data["integrations"]
    for name in ("google_search_console", "dataforseo", "github"):
        if name not in integrations:
            fail(f"integrations missing {name}")
        if "enabled" not in integrations[name]:
            fail(f"integrations.{name} missing enabled")

    print(f"Config valid: {path}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_site_config.py <config-path>", file=sys.stderr)
        raise SystemExit(2)

    validate(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
