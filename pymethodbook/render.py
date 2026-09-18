"""Terminal presentation layer for pymethodbook, built on `rich`.
A single shared Console auto-detects non-terminal output (e.g. piped to a
file or `| cat`) and drops ANSI color codes automatically — no extra
handling needed."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax

console = Console()


def render_method(type_name, method_name, entry):
    """Prints one method's description, signature, and example."""
    code = Syntax(entry["example"], "python", theme="ansi_dark", line_numbers=False)
    panel = Panel(code, title=f"{type_name}.{method_name}", subtitle=entry["signature"])
    console.print(f"[bold]{entry['description']}[/bold]")
    console.print(panel)
    console.print(f"[dim]category: {entry['category']}[/dim]")


def render_type_table(type_name, data):
    """Prints every method for a type as a table, sorted by category then name."""
    table = Table(title=f"{type_name} methods")
    table.add_column("Method", style="bold")
    table.add_column("Signature")
    table.add_column("Category")
    table.add_column("Description")

    for method_name, entry in sorted(data.items(), key=lambda kv: (kv[1]["category"], kv[0])):
        table.add_row(method_name, entry["signature"], entry["category"], entry["description"])

    console.print(table)


def render_search_results(keyword, results):
    """Prints search results across types as a table."""
    if not results:
        console.print(f"[yellow]No matches for '{keyword}'.[/yellow]")
        return

    table = Table(title=f"Search results for '{keyword}'")
    table.add_column("Type", style="bold")
    table.add_column("Method")
    table.add_column("Description")

    for type_name, method_name, entry in results:
        table.add_row(type_name, method_name, entry["description"])

    console.print(table)