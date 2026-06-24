from pathlib import Path

import pytest

from course_utils.notebook_loader import load_notebook_namespace
from homework.hw01.tests.cases import assert_add, assert_greet, assert_is_even


NOTEBOOK = Path(__file__).parents[1] / "homework.ipynb"


@pytest.fixture(scope="module")
def notebook():
    return load_notebook_namespace(NOTEBOOK)


def test_greet(notebook):
    assert "greet" in notebook, "Define a function named greet"
    assert_greet(notebook["greet"])


def test_add(notebook):
    assert "add" in notebook, "Define a function named add"
    assert_add(notebook["add"])


def test_is_even(notebook):
    assert "is_even" in notebook, "Define a function named is_even"
    assert_is_even(notebook["is_even"])
