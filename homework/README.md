# Homework

Each homework folder contains:

- `homework.ipynb`: the student-facing assignment
- `tests/cases.py`: reusable test cases
- `tests/traces.py`: reusable code-trace answers
- `tests/test_notebook.py`: pytest tests that execute the notebook and check the functions

Trace problems should usually ask students to write predicted output as `print(...)` lines. The checker captures that printed output, which keeps the notebook readable and lets GitHub autograde the saved answer.

Start with:

```text
homework/hw01/homework.ipynb
```

HW01 has eight code-trace questions followed by seven beginner programming
questions. The answer cells start with `pass`, so the checks are expected to fail
until the student fills them in.

Each programming function in HW01 has at least five test cases.
