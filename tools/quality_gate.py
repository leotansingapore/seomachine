#!/usr/bin/env python3
"""
Quality gate -- runs before an article moves from review-required/ to published/.

Composite score = weighted avg of SEO quality, readability, and keyword distribution.
Below threshold: article is held in review-required/ with a .score.json sidecar.
Above threshold: article is moved to published/ and the gate returns 0.

Usage:
    python3 tools/quality_gate.py <article.md> [--client <slug>] [--threshold 75]

Exit codes:
    0 -- passed gate, article moved to published/
    1 -- failed gate, article held in review-required/
    2 -- error (missing file, analyzer crash)
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime

# Reuse existing analyzers
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(THIS_DIR, os.pardir))
sys.path.insert(0, REPO_ROOT)
sys.path.insert(0, os.path.join(REPO_ROOT, "data_sources", "modules"))

QUALITY_LOG = os.path.join(REPO_ROOT, "output", "quality-log.jsonl")


def score_article(markdown_path: str) -> dict:
    """Return scores dict using available analyzers; degrade gracefully."""
    with open(markdown_path) as f:
        text = f.read()

    scores = {}

    # SEO quality (0-100) -- fallback to heuristic if analyzer unavailable
    try:
        from seo_quality_rater import rate_content  # type: ignore
        scores["seo"] = float(rate_content(text))
    except Exception:
        # Heuristic: length + headings + internal links
        h2 = text.count("\n## ")
        links = text.count("](")
        words = len(text.split())
        heuristic = min(100, (words / 20) + (h2 * 5) + (links * 2))
        scores["seo"] = round(heuristic, 1)

    # Readability -- Flesch proxy
    try:
        from readability_scorer import flesch_reading_ease  # type: ignore
        scores["readability"] = float(flesch_reading_ease(text))
    except Exception:
        sentences = max(1, text.count(". ") + text.count("! ") + text.count("? "))
        words = len(text.split())
        syllables = sum(max(1, len([c for c in w if c.lower() in "aeiou"])) for w in text.split())
        try:
            flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / max(1, words))
        except Exception:
            flesch = 50.0
        scores["readability"] = round(max(0, min(100, flesch)), 1)

    # Keyword distribution (0-100)
    try:
        from keyword_analyzer import distribution_score  # type: ignore
        scores["keywords"] = float(distribution_score(text))
    except Exception:
        scores["keywords"] = 70.0  # neutral default when analyzer missing

    # Composite -- weighted
    scores["composite"] = round(
        scores["seo"] * 0.5 + scores["readability"] * 0.25 + scores["keywords"] * 0.25,
        1,
    )
    return scores


def log_score(markdown_path: str, client: str, scores: dict, passed: bool) -> None:
    os.makedirs(os.path.dirname(QUALITY_LOG), exist_ok=True)
    entry = {
        "date": datetime.now().isoformat(),
        "article": os.path.relpath(markdown_path, REPO_ROOT),
        "client": client or "",
        "scores": scores,
        "composite": scores["composite"],
        "passed": passed,
    }
    with open(QUALITY_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Quality gate for seomachine articles")
    parser.add_argument("article", help="Path to the article markdown file")
    parser.add_argument("--client", default="", help="Client slug (optional)")
    parser.add_argument("--threshold", type=float, default=75.0, help="Composite score threshold (default 75)")
    args = parser.parse_args()

    if not os.path.isfile(args.article):
        print(f"ERROR: article not found: {args.article}", file=sys.stderr)
        return 2

    try:
        scores = score_article(args.article)
    except Exception as e:
        print(f"ERROR: scoring crashed: {e}", file=sys.stderr)
        return 2

    passed = scores["composite"] >= args.threshold
    log_score(args.article, args.client, scores, passed)

    # Write sidecar
    sidecar = args.article.replace(".md", ".score.json")
    with open(sidecar, "w") as f:
        json.dump({"scores": scores, "threshold": args.threshold, "passed": passed}, f, indent=2)

    print(f"Composite: {scores['composite']:.1f} (threshold {args.threshold})")
    for k in ("seo", "readability", "keywords"):
        print(f"  {k}: {scores[k]:.1f}")

    if not passed:
        print(f"GATE FAIL -- article held. Sidecar: {sidecar}")
        return 1

    # Move to published/
    if args.client:
        dest_dir = os.path.join(REPO_ROOT, "clients", args.client, "published")
    else:
        dest_dir = os.path.join(REPO_ROOT, "published")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, os.path.basename(args.article))
    shutil.move(args.article, dest)
    # Move sidecar alongside
    new_sidecar = dest.replace(".md", ".score.json")
    shutil.move(sidecar, new_sidecar)
    print(f"GATE PASS -- moved to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
