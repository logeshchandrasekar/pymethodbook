"""Command-line interface for pymethodbook."""
import typer

from . import explain as _explain, enlist as _enlist, search as _search
from .core import TypeNotFoundError, MethodNotFoundError

app = typer.Typer(help="A terminal-first reference tool for Python's built-in methods.")


@app.command()
def explain(
    type_name: str = typer.Argument(..., help="e.g. list, dict"),
    method_name: str = typer.Argument(..., help="e.g. append, get"),
):
    """Show one method's description, signature, and example."""
    try:
        _explain(type_name, method_name)
    except (TypeNotFoundError, MethodNotFoundError) as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)


@app.command(name="list")
def list_methods(type_name: str = typer.Argument(..., help="e.g. list, dict")):
    """List every curated method for a type."""
    try:
        _enlist(type_name)
    except TypeNotFoundError as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)


@app.command()
def search(keyword: str = typer.Argument(..., help="Keyword to search for")):
    """Search every type for a keyword."""
    _search(keyword)


if __name__ == "__main__":
    app()