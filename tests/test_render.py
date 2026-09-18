from pymethodbook.render import render_method, render_type_table, render_search_results
from pymethodbook.core import get_method, load_type, search


def test_render_method_runs_without_error():
    entry = get_method("list", "append")
    render_method("list", "append", entry)


def test_render_type_table_runs_without_error():
    data = load_type("dict")
    render_type_table("dict", data)


def test_render_search_results_runs_without_error():
    results = search("copy")
    render_search_results("copy", results)