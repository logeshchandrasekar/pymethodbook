# pymethodbook

A terminal-first reference tool for Python's built-in methods — curated descriptions, runnable examples, and a searchable CLI. No more digging through docs for what `list.sort()` actually does.

## Why

`dir()` and `help()` give you names and terse docstrings. pymethodbook gives you a one-line description, a runnable example, and a category tag for every method — right in your terminal, in code or from the command line.

## Install

```bash
pip install pymethodbook
```

## Usage

### As a CLI

```bash
pymethodbook explain list append
pymethodbook list dict
pymethodbook search copy
```

### As a library

```python
from pymethodbook import explain, enlist, search

explain("list", "append")
enlist("dict")
search("copy")
```

## Currently covers

- `list` — 11 methods
- `dict` — 11 methods

More types (`str`, `set`, `tuple`) are on the roadmap — see [ROADMAP.md](ROADMAP.md).

## Contributing

Adding a method doesn't require touching any Python code — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).