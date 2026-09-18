import json
from pathlib import Path

import pytest

DATA_DIR = Path(__file__).parent.parent / "pymethodbook" / "data"
REQUIRED_KEYS = {"signature", "description", "example", "category"}


def load_all_entries():
    entries = []
    for path in DATA_DIR.glob("*.json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for method_name, entry in data.items():
            entries.append((path.name, method_name, entry))
    return entries


@pytest.mark.parametrize("filename,method_name,entry", load_all_entries())
def test_entry_has_required_keys(filename, method_name, entry):
    missing = REQUIRED_KEYS - entry.keys()
    assert not missing, f"{filename}::{method_name} missing {missing}"


@pytest.mark.parametrize("filename,method_name,entry", load_all_entries())
def test_entry_fields_not_empty(filename, method_name, entry):
    for key in REQUIRED_KEYS:
        assert str(entry.get(key, "")).strip(), f"{filename}::{method_name} has an empty '{key}'"