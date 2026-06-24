# Yisen Coding

This repo is for learning Python with a mix of lessons, Jupyter notebooks, and automatic tests.

The basic idea:

1. Lessons can use notebooks because notebooks are great for explanations, examples, and small experiments.
2. Homework can also use notebooks so each assignment has text, examples, and code cells in one place.
3. Each function can have checks that run immediately inside Jupyter.
4. The same homework can also be checked by `pytest`.
5. When homework is pushed to GitHub, GitHub Actions can run the tests online and show a green check or red X.

## Install The Project

You only need to install `uv` once. After that, `uv` installs Python packages for this project.

If you already cloned the project, go into the folder:

```bash
cd yisen-coding
```

If you are setting it up from GitHub for the first time:

```bash
git clone <repo-url>
cd yisen-coding
```

Then install the project tools:

```bash
uv sync
```

This creates a local `.venv` folder and installs the packages listed in `pyproject.toml`, including:

- `jupyterlab`: opens and runs notebooks
- `ipykernel`: lets notebooks use this project's Python environment
- `pytest`: runs homework tests

## Check The Setup

Run this from the project folder:

```bash
uv run python --version
```

You should see Python 3.12 or newer.

Then check that the main tools are installed:

```bash
uv run python -c "import pytest, jupyterlab, ipykernel; print('Setup OK')"
```

You should see:

```text
Setup OK
```

You can also check the current sample Python file:

```bash
uv run python main.py
```

## Open Jupyter

Start JupyterLab:

```bash
uv run jupyter lab
```

This should open a browser window. If it does not open automatically, the terminal will show a local URL that starts with something like:

```text
http://localhost:8888/lab
```

Open that URL in your browser.

## Homework Plan

Each homework will eventually look something like this:

```text
homework/
  hw01/
    homework.ipynb
    tests/
      cases.py
      test_notebook.py
```

The notebook will contain:

- explanation cells
- examples
- function cells where the student writes code
- check cells or decorators that give immediate feedback

Example function cell:

```python
from course_utils.notebook_check import check

@check("add", "homework.hw01.tests.cases")
def add(a, b):
    return a + b
```

When that cell runs, it can immediately print something like:

```text
[PASS] add: 2/2 tests passed
```

or:

```text
[FAIL] add: 1/2 tests passed
 - add(-1, 1): expected 0, got None
```

So the student can get feedback directly in Jupyter without using the command line every time.

## Run Tests Locally

After homework test files exist, you can run all tests from the terminal:

```bash
uv run pytest -q
```

Or run tests for one homework:

```bash
uv run pytest -q homework/hw01
```

`pytest` finds files named like:

```text
test_something.py
```

and runs functions named like:

```python
def test_something():
    ...
```

Most tests use `assert`.

Example:

```python
def test_add():
    assert add(2, 3) == 5
```

If the answer is correct, the test passes. If not, `pytest` shows what failed.

## How GitHub Checks Homework

Local checks happen on the student's computer.

GitHub checks happen after the student saves, commits, and pushes:

```bash
git add .
git commit -m "Finish hw01"
git push
```

Then GitHub Actions can automatically:

1. download the repo
2. install Python
3. run `uv sync`
4. run `uv run pytest -q`
5. show a green check if tests pass, or a red X if tests fail

The GitHub Actions file will eventually live here:

```text
.github/workflows/tests.yml
```

Example workflow:

```yaml
name: Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: uv sync

      - name: Run tests
        run: uv run pytest -q
```

The student does not need to push to test locally. Pushing is only needed when we want GitHub to check the saved work online.

## Student Workflow

For normal homework:

1. Pull the newest files:

   ```bash
   git pull
   ```

2. Start Jupyter:

   ```bash
   uv run jupyter lab
   ```

3. Open the homework notebook.
4. Read the instructions.
5. Fill in the function cells.
6. Run the cells to see immediate feedback.
7. Before submitting, restart the notebook kernel and run all cells from the top.
8. Push the finished work:

   ```bash
   git add .
   git commit -m "Finish homework"
   git push
   ```

9. Check GitHub for the green check.

## Teacher Workflow

For each homework:

1. Create the notebook instructions.
2. Create the public test cases.
3. Add immediate notebook checks.
4. Add `pytest` tests that execute the saved notebook.
5. Push the assignment.
6. Ask the student to pull the newest version.

The important rule for notebook homework:

Before submitting, restart the kernel and run all cells from top to bottom. This makes sure the saved notebook works cleanly and does not depend on hidden notebook state.

## Troubleshooting

If `uv sync` fails, make sure you are inside the project folder:

```bash
pwd
```

You should be in the folder that contains `pyproject.toml`.

If Jupyter does not start, try:

```bash
uv run jupyter lab --version
```

If a notebook says it cannot find a package, run:

```bash
uv sync
```

If tests behave strangely inside Jupyter, restart the kernel and run all cells again.

If GitHub fails but local tests pass, make sure the notebook was saved before committing:

```bash
git status
```

If there are changed files, save, commit, and push again.
