"""Core text statistics used by the loop-lab CLI."""

from __future__ import annotations

import re

_WORD_RE = re.compile(r"[A-Za-z0-9']+")


def word_count(text: str) -> int:
    """Count words (runs of letters, digits, or apostrophes)."""
    return len(_WORD_RE.findall(text))


def char_count(text: str, include_whitespace: bool = True) -> int:
    """Count characters, optionally excluding whitespace."""
    if include_whitespace:
        return len(text)
    return len("".join(text.split()))


def line_count(text: str) -> int:
    """Count lines. Empty text has zero lines."""
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)
