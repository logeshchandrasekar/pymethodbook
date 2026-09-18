# Contributing to pymethodbook

Thanks for considering a contribution! The easiest way to help is adding a new method entry — it requires zero Python knowledge.

## Adding a method

1. Open the relevant file in `pymethodbook/data/` (e.g. `list.json` for a list method). If the type doesn't have a file yet, create one.
2. Add an entry following this exact shape:

​```json
"method_name": {
  "signature": "type.method_name(args)",
  "description": "One clear sentence on what it does.",
  "example": "input_code\n# -> expected_output",
  "category": "mutating | read-only"
}
​```

3. Validate it:

​```bash
python scripts/validate_data.py
​```

4. Run the test suite to confirm nothing broke:

​```bash
python -m pytest tests/
​```

5. Open a pull request. Please keep one method (or one type file) per PR so it's easy to review.

## Adding a new type (e.g. `str`, `set`)

1. Create `pymethodbook/data/<type>.json` following the schema above.
2. Run `python scripts/validate_data.py` — it automatically picks up any new JSON file in `data/`.
3. No changes needed to `core.py`, `render.py`, or `cli.py` — they already work generically across every file in `data/`.

## Reporting bugs or suggesting features

Open a GitHub issue with a clear description and, for bugs, the exact command you ran and what happened.