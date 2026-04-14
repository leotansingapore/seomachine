#!/usr/bin/env python3
"""
Unified research CLI for seomachine.

Dispatches to the existing research_*.py and seo_*.py scripts via subcommands,
so new clients have one tool to learn.

Usage:
    python3 research.py <subcommand> [args...]
    python3 research.py --help

Subcommands map 1:1 to existing top-level scripts:

  serp                -> research_serp_analysis.py
  gaps                -> research_competitor_gaps.py
  trending            -> research_trending.py
  performance         -> research_performance_matrix.py
  topics              -> research_topic_clusters.py
  priorities          -> research_priorities_comprehensive.py
  quick-wins          -> research_quick_wins.py
  baseline            -> seo_baseline_analysis.py
  competitor          -> seo_competitor_analysis.py
  bofu                -> seo_bofu_rankings.py
  dataforseo-test     -> test_dataforseo.py
"""

import os
import runpy
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

SUBCOMMANDS = {
    "serp":            "research_serp_analysis.py",
    "gaps":            "research_competitor_gaps.py",
    "trending":        "research_trending.py",
    "performance":     "research_performance_matrix.py",
    "topics":          "research_topic_clusters.py",
    "priorities":      "research_priorities_comprehensive.py",
    "quick-wins":      "research_quick_wins.py",
    "baseline":        "seo_baseline_analysis.py",
    "competitor":      "seo_competitor_analysis.py",
    "bofu":            "seo_bofu_rankings.py",
    "dataforseo-test": "test_dataforseo.py",
}


def print_help() -> None:
    print(__doc__)
    print("Available subcommands:")
    for name, script in SUBCOMMANDS.items():
        path = os.path.join(REPO_ROOT, script)
        present = " " if os.path.exists(path) else "*"
        print(f"  {present} {name:20s} -> {script}")
    print("\n* = script file missing")


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
        return 0

    sub = sys.argv[1]
    if sub not in SUBCOMMANDS:
        print(f"ERROR: unknown subcommand: {sub}", file=sys.stderr)
        print_help()
        return 2

    script = os.path.join(REPO_ROOT, SUBCOMMANDS[sub])
    if not os.path.exists(script):
        print(f"ERROR: script not found: {script}", file=sys.stderr)
        return 2

    # Rewrite argv so the target script sees its own args
    sys.argv = [script] + sys.argv[2:]
    runpy.run_path(script, run_name="__main__")
    return 0


if __name__ == "__main__":
    sys.exit(main())
