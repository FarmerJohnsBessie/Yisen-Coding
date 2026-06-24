# Yisen Coding

This repo is for learning Python with a mix of lessons, Jupyter notebooks, and automatic tests.

The basic idea:

1. Lessons can use notebooks because notebooks are great for explanations, examples, and small experiments.
2. Homework can also use notebooks so each assignment has text, examples, and code cells in one place.
3. Each function can have checks that run immediately inside Jupyter.
4. The same homework can also be checked by `pytest`.
5. When homework is pushed to GitHub, GitHub Actions can run the tests online and show a green check or red X.

## Project Structure

The repo now has a working example lesson and homework:

```text
yisen-coding/
  .github/
    workflows/
      tests.yml
  course_utils/
    notebook_check.py
    notebook_loader.py
  lectures/
    01_functions_and_tests/
      notes.ipynb
  homework/
    hw01/
      homework.ipynb
      tests/
        cases.py
        traces.py
        test_notebook.py
  main.py
  pyproject.toml
  uv.lock
```

What each part is for:

- `lectures/`: notebooks used during class
- `homework/`: notebooks the student completes
- `course_utils/notebook_check.py`: the decorator that gives instant feedback in Jupyter
- `course_utils/notebook_loader.py`: the helper that lets `pytest` execute a saved notebook
- `.github/workflows/tests.yml`: the GitHub Actions workflow that runs tests after a push
- `pyproject.toml`: Python version, package dependencies, and pytest settings
- `uv.lock`: the locked dependency versions used by `uv`

This project intentionally avoids extra `__init__.py` files. Modern Python can import these folders as namespace packages, and fewer marker files makes the course easier to navigate.

The test command uses `python -B` so Python does not create `__pycache__` folders while running homework checks.

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

## VS Code Or Browser Jupyter?

Both are okay.

For teaching, the browser version from `uv run jupyter lab` is usually simpler because everyone sees the same Jupyter interface. Use this when you want fewer setup surprises.

VS Code notebooks are also fine, especially if the student is already comfortable in VS Code. If using VS Code:

1. Open the whole `yisen-coding` folder, not just one notebook file.
2. Open the homework notebook.
3. Click the kernel selector in the top right.
4. Choose the Python environment from this project, usually `.venv`.

The most common mistake is opening the notebook with the wrong working directory or wrong Python kernel. If that happens, imports like this may fail:

```python
from course_utils.notebook_check import check
```

The homework setup cell now searches for the project root automatically, but VS Code should still be opened at the project folder for the smoothest experience.

## Example Class Flow

A normal class can work like this:

1. Open a lecture notebook, such as `lectures/01_functions_and_tests/notes.ipynb`.
2. Teach the concept with examples and small live-coding changes.
3. Open the homework notebook, such as `homework/hw01/homework.ipynb`.
4. The student fills in one function at a time.
5. Every function cell has a decorator like `@check(...)`.
6. When the student runs that cell, Jupyter immediately prints pass/fail feedback.
7. At the end, the student saves the notebook and runs the final pytest cell inside the notebook.
8. Before submitting, the student restarts the kernel and runs all cells from the top.
9. The student commits and pushes.
10. GitHub Actions runs the same tests online.

## Homework Structure

The sample homework is here:

```text
homework/
  hw01/
    homework.ipynb
    tests/
      cases.py
      traces.py
      test_notebook.py
```

The notebook contains:

- explanation cells
- examples
- function cells where the student writes code
- trace cells where the student predicts code output
- check cells or decorators that give immediate feedback

Example function cell from `homework/hw01/homework.ipynb`:

```python
from course_utils.notebook_check import check

@check("add", "homework.hw01.tests.cases")
def add(a, b):
    return a + b
```

When that cell runs, it can immediately print something like:

```text
AC  Test case 1 passed
AC  Test case 2 passed
AC  Test case 3 passed
[PASS] add: 3/3 tests passed
```

or:

```text
AC  Test case 1 passed
WA  Test case 2 failed: add(-1, 1) - expected 0, got None
[FAIL] add: 1/2 tests passed
```

So the student can get feedback directly in Jupyter without using the command line every time.

The test cases live in `homework/hw01/tests/cases.py`. Both the notebook decorator and the pytest tests reuse those same cases.

Code-trace answers live in `homework/hw01/tests/traces.py`. Trace checks use simpler pass/fail output so wrong answers do not reveal the expected answer.

For trace problems, the student writes the predicted output with `print(...)` lines:

```python
@trace("basics", "homework.hw01.tests.traces")
def basics():
    print(0)
    print(1)
```

The checker captures the printed output and compares it with the expected output. This is easier to read than triple-quoted strings, and GitHub can autograde it because the answer is saved in the notebook source.

Trace feedback does not show the expected answer when the student is wrong:

```text
WA  Trace failed
[FAIL] basics: 0/1 tests passed
```

The pytest file `homework/hw01/tests/test_notebook.py` opens the saved `homework.ipynb`, runs the code cells from top to bottom, and then checks that the expected functions exist and behave correctly.

## Run Tests Locally

You can run all tests from the terminal:

```bash
uv run python -B -m pytest -q
```

Or run tests for one homework:

```bash
uv run python -B -m pytest -q homework/hw01
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

The student can also run the final check from inside the homework notebook. That cell calls `pytest` for the current homework, so the student does not need the command line for normal practice. Save the notebook before running the final check, because `pytest` reads the saved `.ipynb` file from disk.

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
3. run `uv sync --locked`
4. run `uv run python -B -m pytest -q`
5. show a green check if tests pass, or a red X if tests fail

The GitHub Actions file already lives here:

```text
.github/workflows/tests.yml
```

Current workflow:

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
        run: uv sync --locked

      - name: Run tests
        run: uv run python -B -m pytest -q
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
7. Save the notebook.
8. Run the final pytest cell in the notebook.
9. Before submitting, restart the notebook kernel and run all cells from the top.
10. Push the finished work:

   ```bash
   git add .
   git commit -m "Finish homework"
   git push
   ```

11. Check GitHub for the green check.

## Teacher Workflow

For each homework:

1. Copy an existing homework folder, such as `homework/hw01`.
2. Rename it to the next homework, such as `homework/hw02`.
3. Update the notebook instructions.
4. Update `tests/cases.py` with the new cases.
5. Update `tests/traces.py` with any code-trace answers.
6. Update `tests/test_notebook.py` with the expected function and trace names.
7. Run `uv run python -B -m pytest -q`.
8. Push the assignment.
9. Ask the student to pull the newest version.

The important rule for notebook homework:

Before submitting, restart the kernel and run all cells from top to bottom. This makes sure the saved notebook works cleanly and does not depend on hidden notebook state.

When the course structure changes, update this README in the same change. The README should always explain the current student workflow, not an old version of the workflow.

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

If the notebook says `ModuleNotFoundError: No module named 'course_utils'`, check these things:

1. Make sure you opened the `yisen-coding` folder, not just the `.ipynb` file.
2. Make sure the selected notebook kernel is the project `.venv`.
3. In browser Jupyter, make sure you started Jupyter from the project folder:

   ```bash
   cd yisen-coding
   uv run jupyter lab
   ```

4. Restart the notebook kernel and run the setup cell again.

If tests behave strangely inside Jupyter, restart the kernel and run all cells again.

If GitHub fails but local tests pass, make sure the notebook was saved before committing:

```bash
git status
```

If there are changed files, save, commit, and push again.
