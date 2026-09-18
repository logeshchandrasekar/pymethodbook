"""Validates every JSON file in pymethodbook/data/.

Usage: python scripts/validate_data.py
Exits with status 1 if any entry is missing or has an empty required field.
"""
import json
import sys
from pathlib import Path

REQUIRED_KEYS = ("signature", "description", "example", "category")
DATA_DIR = Path(__file__).parent.parent / "pymethodbook" / "data"


def validate_file(path):
    errors = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    for method_name, entry in data.items():
        for key in REQUIRED_KEYS:
            if key not in entry:
                errors.append(f"{path.name}::{method_name} missing '{key}'")
            elif not str(entry[key]).strip():
                errors.append(f"{path.name}::{method_name} has an empty '{key}'")
    return len(data), errors


def main():
    json_files = sorted(DATA_DIR.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {DATA_DIR}")
        return 1

    all_errors = []
    for path in json_files:
        count, errors = validate_file(path)
        status = "OK" if not errors else "FAILED"
        print(f"{path.name}: {status} ({count} methods)")
        all_errors.extend(errors)

    if all_errors:
        print("\nErrors found:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("\nAll data files valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())