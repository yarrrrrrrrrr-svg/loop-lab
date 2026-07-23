"""Command-line interface for loop-lab."""

from __future__ import annotations

import argparse
import sys

from loop_lab.textstats import char_count, line_count, word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="loop-lab", description="Tiny text-stats CLI.")
    parser.add_argument("file", nargs="?", help="File to analyze; reads stdin if omitted.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.file:
        with open(args.file, encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()
    print(f"lines: {line_count(text)}")
    print(f"words: {word_count(text)}")
    print(f"chars: {char_count(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
