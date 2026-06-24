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

For this sample homework, the functions are already solved so the workflow passes. For a real assignment, replace the function bodies with `pass` or a `TODO` starter.
