# Homework

Each homework folder contains:

- `homework.ipynb`: the student-facing assignment
- `tests/cases.py`: reusable test cases
- `tests/traces.py`: reusable code-trace answers
- `tests/test_notebook.py`: pytest tests that execute the notebook and check the functions

Trace problems should usually ask students to write predicted output as `print(...)` lines. The checker captures that printed output, which keeps the notebook readable and lets GitHub autograde the saved answer.

Start with:

```text
homework/hw00/homework.ipynb
homework/hw01/homework.ipynb
```

HW00 is the in-class demo homework. It has two code-trace questions and two
very simple programming questions so the student can practice running cells,
reading checker output, saving the notebook, and running the final check.

HW01 has eight code-trace questions followed by seven beginner programming
questions. The answer cells start with `pass`, so the checks are expected to fail
until the student fills them in.

Each programming function in HW01 has at least five test cases.

Each assignment notebook ends with a "Submit This Homework" section. The student
should copy those exact commands for the current homework, especially the
homework-specific path like `homework/hw01/homework.ipynb`.
