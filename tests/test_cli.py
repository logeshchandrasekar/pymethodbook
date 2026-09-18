from typer.testing import CliRunner

from pymethodbook.cli import app

runner = CliRunner()


def test_explain_known_method_succeeds():
    result = runner.invoke(app, ["explain", "list", "append"])
    assert result.exit_code == 0


def test_explain_unknown_type_fails_cleanly():
    result = runner.invoke(app, ["explain", "banana", "append"])
    assert result.exit_code == 1


def test_explain_typo_method_fails_cleanly():
    result = runner.invoke(app, ["explain", "list", "apend"])
    assert result.exit_code == 1


def test_list_command_succeeds():
    result = runner.invoke(app, ["list", "dict"])
    assert result.exit_code == 0


def test_list_unknown_type_fails_cleanly():
    result = runner.invoke(app, ["list", "banana"])
    assert result.exit_code == 1


def test_search_command_succeeds():
    result = runner.invoke(app, ["search", "copy"])
    assert result.exit_code == 0