"""Tests for tools/mastering/reference_master.py."""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

# Import the module under test
_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

# Force-mock matchering before importing the module so tests behave
# consistently regardless of whether matchering is installed.
_MOCK_DEPS = ["matchering"]
_SAVED_DEPS = {dep: sys.modules.get(dep) for dep in _MOCK_DEPS}
for dep in _MOCK_DEPS:
    sys.modules[dep] = MagicMock()

from tools.mastering import reference_master as mod

# Restore original modules to avoid polluting later tests
for dep, original in _SAVED_DEPS.items():
    if original is None:
        sys.modules.pop(dep, None)
    else:
        sys.modules[dep] = original


# ---------------------------------------------------------------------------
# master_with_reference
# ---------------------------------------------------------------------------

@pytest.mark.unit
class TestMasterWithReference:
    """Tests for reference-based mastering via matchering."""

    def test_calls_mg_process(self, tmp_path):
        target = tmp_path / "track.wav"
        target.write_bytes(b"audio")
        reference = tmp_path / "ref.wav"
        reference.write_bytes(b"ref audio")
        output = tmp_path / "mastered" / "track.wav"
        output.parent.mkdir()

        mod.master_with_reference(target, reference, output)

        mod.mg.process.assert_called_once()

    def test_passes_paths_as_strings(self, tmp_path):
        target = tmp_path / "track.wav"
        target.write_bytes(b"audio")
        reference = tmp_path / "ref.wav"
        reference.write_bytes(b"ref audio")
        output = tmp_path / "out.wav"

        mod.master_with_reference(target, reference, output)

        args, kwargs = mod.mg.process.call_args
        assert kwargs["target"] == str(target)
        assert kwargs["reference"] == str(reference)

    def test_uses_pcm16_output(self, tmp_path):
        target = tmp_path / "track.wav"
        target.write_bytes(b"audio")
        reference = tmp_path / "ref.wav"
        reference.write_bytes(b"ref audio")
        output = tmp_path / "out.wav"

        mod.master_with_reference(target, reference, output)

        args, kwargs = mod.mg.process.call_args
        # results should contain a pcm16() call
        assert "results" in kwargs
        mod.mg.pcm16.assert_called_with(str(output))

    def test_matchering_exception_propagates(self, tmp_path):
        target = tmp_path / "track.wav"
        target.write_bytes(b"audio")
        reference = tmp_path / "ref.wav"
        reference.write_bytes(b"ref audio")
        output = tmp_path / "out.wav"

        mod.mg.process.side_effect = RuntimeError("matchering failed")
        with pytest.raises(RuntimeError, match="matchering failed"):
            mod.master_with_reference(target, reference, output)
        # Reset side_effect for other tests
        mod.mg.process.side_effect = None


# ---------------------------------------------------------------------------
# main() CLI
# ---------------------------------------------------------------------------

@pytest.mark.unit
class TestMain:
    """Tests for reference_master CLI entry point."""

    @patch.object(mod, "master_with_reference")
    def test_single_file_mode(self, mock_master, tmp_path, monkeypatch):
        ref = tmp_path / "reference.wav"
        ref.write_bytes(b"ref")
        target = tmp_path / "target.wav"
        target.write_bytes(b"target")
        out_dir = tmp_path / "mastered"

        monkeypatch.setattr(
            "sys.argv",
            ["reference_master.py", "--reference", str(ref), "--target", str(target),
             "--output-dir", str(out_dir)],
        )
        mod.main()
        mock_master.assert_called_once()
        assert out_dir.exists()

    @patch.object(mod, "master_with_reference")
    def test_batch_mode(self, mock_master, tmp_path, monkeypatch):
        # Put reference outside the working dir so it doesn't get globbed
        ref = tmp_path / "refs" / "reference.wav"
        ref.parent.mkdir()
        ref.write_bytes(b"ref")
        work_dir = tmp_path / "tracks"
        work_dir.mkdir()
        monkeypatch.chdir(work_dir)
        (work_dir / "track1.wav").write_bytes(b"t1")
        (work_dir / "track2.wav").write_bytes(b"t2")

        monkeypatch.setattr(
            "sys.argv",
            ["reference_master.py", "--reference", str(ref),
             "--output-dir", str(tmp_path / "mastered")],
        )
        mod.main()
        assert mock_master.call_count == 2

    def test_missing_reference_exits(self, tmp_path, monkeypatch):
        monkeypatch.setattr(
            "sys.argv",
            ["reference_master.py", "--reference", str(tmp_path / "missing.wav")],
        )
        with pytest.raises(SystemExit):
            mod.main()
