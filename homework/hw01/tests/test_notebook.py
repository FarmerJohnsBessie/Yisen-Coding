from pathlib import Path

import pytest

from course_utils.notebook_loader import load_notebook_namespace
from homework.hw01.tests.cases import (
    assert_average_score,
    assert_can_enter_contest,
    assert_double,
    assert_full_groups,
    assert_is_even,
    assert_rectangle_area,
    assert_total_seconds,
)
from homework.hw01.tests.traces import (
    assert_boolean_logic_a,
    assert_boolean_logic_b,
    assert_conversions,
    assert_exponent_update,
    assert_floor_division,
    assert_mod_remainders,
    assert_type_checks,
    assert_update_number,
)


NOTEBOOK = Path(__file__).parents[1] / "homework.ipynb"


@pytest.fixture(scope="module")
def notebook():
    return load_notebook_namespace(NOTEBOOK)


def test_mod_remainders_trace(notebook):
    assert "mod_remainders" in notebook, "Define a trace answer named mod_remainders"
    assert_mod_remainders(notebook["mod_remainders"])


def test_floor_division_trace(notebook):
    assert "floor_division" in notebook, "Define a trace answer named floor_division"
    assert_floor_division(notebook["floor_division"])


def test_boolean_logic_a_trace(notebook):
    assert "boolean_logic_a" in notebook, "Define a trace answer named boolean_logic_a"
    assert_boolean_logic_a(notebook["boolean_logic_a"])


def test_exponent_update_trace(notebook):
    assert "exponent_update" in notebook, "Define a trace answer named exponent_update"
    assert_exponent_update(notebook["exponent_update"])


def test_type_checks_trace(notebook):
    assert "type_checks" in notebook, "Define a trace answer named type_checks"
    assert_type_checks(notebook["type_checks"])


def test_update_number_trace(notebook):
    assert "update_number" in notebook, "Define a trace answer named update_number"
    assert_update_number(notebook["update_number"])


def test_boolean_logic_b_trace(notebook):
    assert "boolean_logic_b" in notebook, "Define a trace answer named boolean_logic_b"
    assert_boolean_logic_b(notebook["boolean_logic_b"])


def test_conversions_trace(notebook):
    assert "conversions" in notebook, "Define a trace answer named conversions"
    assert_conversions(notebook["conversions"])


def test_double(notebook):
    assert "double" in notebook, "Define a function named double"
    assert_double(notebook["double"])


def test_rectangle_area(notebook):
    assert "rectangle_area" in notebook, "Define a function named rectangle_area"
    assert_rectangle_area(notebook["rectangle_area"])


def test_average_score(notebook):
    assert "average_score" in notebook, "Define a function named average_score"
    assert_average_score(notebook["average_score"])


def test_full_groups(notebook):
    assert "full_groups" in notebook, "Define a function named full_groups"
    assert_full_groups(notebook["full_groups"])


def test_is_even(notebook):
    assert "is_even" in notebook, "Define a function named is_even"
    assert_is_even(notebook["is_even"])


def test_total_seconds(notebook):
    assert "total_seconds" in notebook, "Define a function named total_seconds"
    assert_total_seconds(notebook["total_seconds"])


def test_can_enter_contest(notebook):
    assert "can_enter_contest" in notebook, "Define a function named can_enter_contest"
    assert_can_enter_contest(notebook["can_enter_contest"])
