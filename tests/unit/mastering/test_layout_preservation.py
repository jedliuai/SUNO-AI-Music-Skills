"""Tests for LAYOUT.md hand-edit preservation (#290 phase 6, step 7)."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.mastering.layout import (  # noqa: E402
    compute_transitions,
    parse_layout_yaml,
    render_layout_markdown,
)


# ---------------------------------------------------------------------------
# parse_layout_yaml
# ---------------------------------------------------------------------------


def test_parse_layout_yaml_extracts_transitions() -> None:
    """Round-trip: render → parse → transitions match."""
    transitions = [
        {
            "from": "01-a.wav",
            "to": "02-b.wav",
            "mode": "gapless",
            "gap_ms": 0,
            "tail_fade_ms": 0,
            "head_fade_ms": 0,
        },
        {
            "from": "02-b.wav",
            "to": "03-c.wav",
            "mode": "gap",
            "gap_ms": 2000,
            "tail_fade_ms": 100,
            "head_fade_ms": 50,
        },
    ]
    md = render_layout_markdown("my-album", transitions)
    result = parse_layout_yaml(md)
    assert result == transitions


def test_parse_layout_yaml_returns_empty_on_missing_block() -> None:
    """Markdown with no yaml fenced block returns []."""
    md = "# Album Layout\n\nNo yaml block here.\n"
    assert parse_layout_yaml(md) == []


def test_parse_layout_yaml_returns_empty_on_bad_yaml() -> None:
    """Malformed yaml inside the fence returns []."""
    md = "```yaml\n: this is not valid yaml: [\n```\n"
    assert parse_layout_yaml(md) == []


def test_parse_layout_yaml_returns_empty_on_no_transitions_key() -> None:
    """Valid yaml but missing 'transitions' key returns []."""
    md = "```yaml\nother_key: value\n```\n"
    assert parse_layout_yaml(md) == []


def test_parse_layout_yaml_returns_empty_on_transitions_not_list() -> None:
    """'transitions' present but not a list returns []."""
    md = "```yaml\ntransitions: null\n```\n"
    assert parse_layout_yaml(md) == []


# ---------------------------------------------------------------------------
# compute_transitions — prior_transitions preservation
# ---------------------------------------------------------------------------


def test_compute_transitions_preserves_hand_edits() -> None:
    """Prior gapless 01→02 is kept; prior gap 02→03 with gap_ms=2000 is kept."""
    prior = [
        {
            "from": "01-a.wav",
            "to": "02-b.wav",
            "mode": "gapless",
            "gap_ms": 0,
            "tail_fade_ms": 0,
            "head_fade_ms": 0,
        },
        {
            "from": "02-b.wav",
            "to": "03-c.wav",
            "mode": "gap",
            "gap_ms": 2000,
            "tail_fade_ms": 100,
            "head_fade_ms": 50,
        },
    ]
    result = compute_transitions(
        ["01-a.wav", "02-b.wav", "03-c.wav"],
        default_transition="gap",
        prior_transitions=prior,
    )
    assert len(result) == 2
    # 01→02: hand-edited gapless preserved
    assert result[0]["mode"] == "gapless"
    assert result[0]["gap_ms"] == 0
    # 02→03: hand-edited gap_ms=2000 preserved
    assert result[1]["mode"] == "gap"
    assert result[1]["gap_ms"] == 2000


def test_compute_transitions_uses_default_for_new_pairs() -> None:
    """New 02→03 pair (not in prior) uses the computed default."""
    prior = [
        {
            "from": "01-a.wav",
            "to": "02-b.wav",
            "mode": "gapless",
            "gap_ms": 0,
            "tail_fade_ms": 0,
            "head_fade_ms": 0,
        },
    ]
    result = compute_transitions(
        ["01-a.wav", "02-b.wav", "03-c.wav"],
        default_transition="gap",
        prior_transitions=prior,
    )
    assert len(result) == 2
    # 01→02: hand-edited gapless preserved
    assert result[0]["mode"] == "gapless"
    # 02→03: new pair, gets gap default (gap_ms=1500)
    assert result[1]["from"] == "02-b.wav"
    assert result[1]["to"] == "03-c.wav"
    assert result[1]["mode"] == "gap"
    assert result[1]["gap_ms"] == 1500


def test_compute_transitions_drops_stale_pairs() -> None:
    """Prior 02→03 is silently dropped when track 03 is removed."""
    prior = [
        {
            "from": "01-a.wav",
            "to": "02-b.wav",
            "mode": "gapless",
            "gap_ms": 0,
            "tail_fade_ms": 0,
            "head_fade_ms": 0,
        },
        {
            "from": "02-b.wav",
            "to": "03-c.wav",
            "mode": "gap",
            "gap_ms": 2000,
            "tail_fade_ms": 100,
            "head_fade_ms": 50,
        },
    ]
    # Track 03 removed — only two tracks remain.
    result = compute_transitions(
        ["01-a.wav", "02-b.wav"],
        default_transition="gap",
        prior_transitions=prior,
    )
    assert len(result) == 1
    assert result[0]["from"] == "01-a.wav"
    assert result[0]["to"] == "02-b.wav"
    # The 01→02 prior (gapless) is preserved.
    assert result[0]["mode"] == "gapless"
    # The stale 02→03 entry is gone (not in output at all).
    assert all(t["to"] != "03-c.wav" for t in result)
