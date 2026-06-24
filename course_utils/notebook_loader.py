from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SKIP_MARKERS = ("# PYTEST-SKIP", "# AUTOGRADER-SKIP")


def cell_source(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def load_notebook_namespace(path: str | Path) -> dict[str, Any]:
    """Execute a notebook from top to bottom and return its Python namespace."""

    notebook_path = Path(path)
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    namespace: dict[str, Any] = {
        "__name__": "__student_notebook__",
        "__file__": str(notebook_path),
    }

    for index, cell in enumerate(notebook["cells"], start=1):
        if cell.get("cell_type") != "code":
            continue

        source = cell_source(cell)
        if any(marker in source for marker in SKIP_MARKERS):
            continue

        code = compile(source, f"{notebook_path}:cell-{index}", "exec")
        exec(code, namespace)

    return namespace
