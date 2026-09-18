import pytest
from pymethodbook.core import (
    available_types, load_type, get_method, search,
    TypeNotFoundError, MethodNotFoundError,
)


def test_available_types_includes_list_and_dict():
    types = available_types()
    assert "list" in types
    assert "dict" in types


def test_load_type_returns_dict_with_entries():
    data = load_type("list")
    assert "append" in data
    assert "signature" in data["append"]


def test_load_type_unknown_type_raises():
    with pytest.raises(TypeNotFoundError):
        load_type("banana")


def test_get_method_returns_entry():
    entry = get_method("list", "append")
    assert entry["category"] == "mutating"


def test_get_method_typo_suggests_close_match():
    with pytest.raises(MethodNotFoundError) as exc_info:
        get_method("list", "apend")
    assert "append" in str(exc_info.value)


def test_search_finds_exact_method_name():
    results = search("append")
    names = [method for _, method, _ in results]
    assert "append" in names


def test_search_finds_by_description_keyword():
    results = search("shallow copy")
    names = [method for _, method, _ in results]
    assert "copy" in names