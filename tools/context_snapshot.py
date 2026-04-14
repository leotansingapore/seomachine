#!/usr/bin/env python3
"""
Snapshot context/ into context/.snapshots/v<VERSION>/ and bump context/VERSION.

Usage:
    python3 tools/context_snapshot.py "reason for change"

Writes:
    context/.snapshots/v<new>/  -- full copy of current context/ (excluding .snapshots)
    context/VERSION             -- bumped (patch by default, --minor or --major override)
    context/CHANGELOG.md        -- prepended with entry

Rollback:
    cp -r context/.snapshots/v<version>/* context/
"""

import argparse
import os
import shutil
import sys
from datetime import datetime

CONTEXT_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "context")
CONTEXT_DIR = os.path.abspath(CONTEXT_DIR)
VERSION_FILE = os.path.join(CONTEXT_DIR, "VERSION")
CHANGELOG = os.path.join(CONTEXT_DIR, "CHANGELOG.md")
SNAPSHOT_ROOT = os.path.join(CONTEXT_DIR, ".snapshots")


def read_version() -> tuple:
    if not os.path.exists(VERSION_FILE):
        return (0, 1, 0)
    raw = open(VERSION_FILE).read().strip().lstrip("v")
    parts = raw.split(".")
    return tuple(int(p) for p in parts[:3]) + (0,) * (3 - len(parts))


def bump(version: tuple, level: str) -> tuple:
    major, minor, patch = version
    if level == "major":
        return (major + 1, 0, 0)
    if level == "minor":
        return (major, minor + 1, 0)
    return (major, minor, patch + 1)


def snapshot(new_version: str) -> str:
    dest = os.path.join(SNAPSHOT_ROOT, f"v{new_version}")
    if os.path.exists(dest):
        raise SystemExit(f"Snapshot already exists: {dest}")
    os.makedirs(dest, exist_ok=True)
    for name in os.listdir(CONTEXT_DIR):
        if name in (".snapshots", "VERSION", "CHANGELOG.md"):
            continue
        src = os.path.join(CONTEXT_DIR, name)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dest, name))
        else:
            shutil.copy2(src, dest)
    return dest


def prepend_changelog(new_version: str, reason: str) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"## v{new_version} -- {stamp}\n\n- {reason}\n\n"
    existing = ""
    if os.path.exists(CHANGELOG):
        existing = open(CHANGELOG).read()
    else:
        existing = "# Context Changelog\n\nEach entry corresponds to a snapshot under context/.snapshots/v<version>/.\n\n"
    if existing.startswith("# Context Changelog"):
        head, _, rest = existing.partition("\n\n")
        new = f"{head}\n\n{entry}{rest}"
    else:
        new = f"# Context Changelog\n\n{entry}{existing}"
    with open(CHANGELOG, "w") as f:
        f.write(new)


def main() -> int:
    parser = argparse.ArgumentParser(description="Snapshot and version context/ presets")
    parser.add_argument("reason", help="One-line reason for this snapshot")
    parser.add_argument("--major", action="store_true")
    parser.add_argument("--minor", action="store_true")
    args = parser.parse_args()

    level = "major" if args.major else "minor" if args.minor else "patch"
    new = bump(read_version(), level)
    new_version = ".".join(str(n) for n in new)

    dest = snapshot(new_version)
    with open(VERSION_FILE, "w") as f:
        f.write(new_version + "\n")
    prepend_changelog(new_version, args.reason)

    print(f"Snapshot: {dest}")
    print(f"VERSION:  {new_version}")
    print(f"Changelog updated: {CHANGELOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
