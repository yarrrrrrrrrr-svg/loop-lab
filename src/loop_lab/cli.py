"""Command-line interface for loop-lab."""

from __future__ import annotations

import argparse
import json
import sys

from loop_lab.textstats import char_count, line_count, word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="loop-lab", description="Tiny text-stats CLI.")
    parser.add_argument("file", nargs="?", help="File to analyze; reads stdin if omitted.")
    parser.add_argument("--json", action="store_true", help="Output stats as a JSON object.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.file:
        with open(args.file, encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()
    stats = {"lines": line_count(text), "words": word_count(text), "chars": char_count(text)}
    if args.json:
        print(json.dumps(stats))
    else:
        print(f"lines: {stats['lines']}")
        print(f"words: {stats['words']}")
        print(f"chars: {stats['chars']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
