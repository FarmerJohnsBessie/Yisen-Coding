from pathlib import Path

import pytest

from course_utils.notebook_loader import load_notebook_namespace
from homework.hw00.tests.cases import assert_add_numbers, assert_add_one
from homework.hw00.tests.traces import assert_first_prints, assert_variable_update


NOTEBOOK = Path(__file__).parents[1] / "homework.ipynb"


@pytest.fixture(scope="module")
def notebook():
    return load_notebook_namespace(NOTEBOOK)


def test_first_prints_trace(notebook):
    assert "first_prints" in notebook, "Define a trace answer named first_prints"
    assert_first_prints(notebook["first_prints"])


def test_variable_update_trace(notebook):
    assert "variable_update" in notebook, "Define a trace answer named variable_update"
    assert_variable_update(notebook["variable_update"])


def test_add_one(notebook):
    assert "add_one" in notebook, "Define a function named add_one"
    assert_add_one(notebook["add_one"])


def test_add_numbers(notebook):
    assert "add_numbers" in notebook, "Define a function named add_numbers"
    assert_add_numbers(notebook["add_numbers"])
