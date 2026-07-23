import io
import json

from loop_lab.cli import main

SAMPLE = "hello world\nsecond line here\n"


def test_json_flag_with_file(tmp_path, capsys):
    path = tmp_path / "sample.txt"
    path.write_text(SAMPLE, encoding="utf-8")
    assert main(["--json", str(path)]) == 0
    out = capsys.readouterr().out
    assert out.count("\n") == 1
    assert json.loads(out) == {"lines": 2, "words": 5, "chars": 29}


def test_json_flag_with_stdin(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("hello world"))
    assert main(["--json"]) == 0
    out = capsys.readouterr().out
    assert json.loads(out) == {"lines": 1, "words": 2, "chars": 11}


def test_default_output_unchanged(tmp_path, capsys):
    path = tmp_path / "sample.txt"
    path.write_text(SAMPLE, encoding="utf-8")
    assert main([str(path)]) == 0
    assert capsys.readouterr().out == "lines: 2\nwords: 5\nchars: 29\n"


def test_help_lists_json_flag(capsys):
    try:
        main(["--help"])
    except SystemExit:
        pass
    assert "--json" in capsys.readouterr().out
