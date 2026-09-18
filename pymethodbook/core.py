"""Core lookup and search logic for pymethodbook. No printing happens here —
this module only loads and finds data; pymethodbook/render.py displays it."""
import json
import difflib
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


class TypeNotFoundError(Exception):
    """Raised when a requested type has no data file."""


class MethodNotFoundError(Exception):
    """Raised when a requested method isn't found for a type."""


def available_types():
    """Returns a sorted list of supported type names, e.g. ['dict', 'list']."""
    return sorted(p.stem for p in DATA_DIR.glob("*.json"))


def load_type(type_name):
    """Loads and returns the full data dict for a type, e.g. load_type('list')."""
    path = DATA_DIR / f"{type_name}.json"
    if not path.exists():
        types = ", ".join(available_types())
        raise TypeNotFoundError(f"No data for type '{type_name}'. Available types: {types}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_method(type_name, method_name):
    """Returns the entry dict for one method. Raises MethodNotFoundError with
    close-match suggestions if the name is misspelled."""
    data = load_type(type_name)
    if method_name in data:
        return data[method_name]

    close = difflib.get_close_matches(method_name, data.keys(), n=3, cutoff=0.5)
    hint = f" Did you mean: {', '.join(close)}?" if close else ""
    raise MethodNotFoundError(f"'{method_name}' not found on {type_name}.{hint}")


def search(keyword):
    """Searches every type's methods for keyword matches in the name or
    description. Returns a list of (type_name, method_name, entry) tuples —
    exact name matches first, then substring matches, then fuzzy matches."""
    keyword_lower = keyword.lower()
    exact, substring, fuzzy = [], [], []

    for type_name in available_types():
        data = load_type(type_name)
        already = set()

        for method_name, entry in data.items():
            if method_name.lower() == keyword_lower:
                exact.append((type_name, method_name, entry))
                already.add(method_name)
            elif keyword_lower in method_name.lower() or keyword_lower in entry["description"].lower():
                substring.append((type_name, method_name, entry))
                already.add(method_name)

        remaining = [m for m in data if m not in already]
        close = difflib.get_close_matches(keyword_lower, [m.lower() for m in remaining], n=3, cutoff=0.6)
        for method_name in remaining:
            if method_name.lower() in close:
                fuzzy.append((type_name, method_name, data[method_name]))

    return exact + substring + fuzzy