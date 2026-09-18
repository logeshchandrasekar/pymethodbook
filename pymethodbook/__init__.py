"""pymethodbook — a terminal-first reference tool for Python's built-in methods."""
from .core import get_method, load_type, search as _search
from .render import render_method, render_type_table, render_search_results

__version__ = "0.1.0"


def explain(type_name, method_name):
    """Looks up one method and prints it."""
    entry = get_method(type_name, method_name)
    render_method(type_name, method_name, entry)


def enlist(type_name):
    """Prints every curated method for a type."""
    data = load_type(type_name)
    render_type_table(type_name, data)


def search(keyword):
    """Searches every type for a keyword and prints the results."""
    results = _search(keyword)
    render_search_results(keyword, results)