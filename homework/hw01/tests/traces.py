from course_utils.notebook_check import assert_result, run_traces


MOD_REMAINDERS_OUTPUT = [
    "0",
    "3",
    "73",
    "673",
]


def trace_mod_remainders(fn):
    return run_traces(fn, MOD_REMAINDERS_OUTPUT)


def assert_mod_remainders(fn):
    assert_result("mod_remainders", trace_mod_remainders(fn))


FLOOR_DIVISION_OUTPUT = [
    "263",
    "26",
    "2",
    "0",
]


def trace_floor_division(fn):
    return run_traces(fn, FLOOR_DIVISION_OUTPUT)


def assert_floor_division(fn):
    assert_result("floor_division", trace_floor_division(fn))


BOOLEAN_LOGIC_A_OUTPUT = [
    "True",
    "False",
    "False",
    "False",
]


def trace_boolean_logic_a(fn):
    return run_traces(fn, BOOLEAN_LOGIC_A_OUTPUT)


def assert_boolean_logic_a(fn):
    assert_result("boolean_logic_a", trace_boolean_logic_a(fn))


EXPONENT_UPDATE_OUTPUT = [
    "4",
    "16",
    "10",
]


def trace_exponent_update(fn):
    return run_traces(fn, EXPONENT_UPDATE_OUTPUT)


def assert_exponent_update(fn):
    assert_result("exponent_update", trace_exponent_update(fn))


TYPE_CHECKS_OUTPUT = [
    "False",
    "True",
    "False",
]


def trace_type_checks(fn):
    return run_traces(fn, TYPE_CHECKS_OUTPUT)


def assert_type_checks(fn):
    assert_result("type_checks", trace_type_checks(fn))


UPDATE_NUMBER_OUTPUT = [
    "0",
    "1",
    "61.9",
    "61",
]


def trace_update_number(fn):
    return run_traces(fn, UPDATE_NUMBER_OUTPUT)


def assert_update_number(fn):
    assert_result("update_number", trace_update_number(fn))


BOOLEAN_LOGIC_B_OUTPUT = [
    "False",
    "False",
    "False",
]


def trace_boolean_logic_b(fn):
    return run_traces(fn, BOOLEAN_LOGIC_B_OUTPUT)


def assert_boolean_logic_b(fn):
    assert_result("boolean_logic_b", trace_boolean_logic_b(fn))


CONVERSIONS_OUTPUT = [
    "True False",
    "47 True",
    "1 0",
]


def trace_conversions(fn):
    return run_traces(fn, CONVERSIONS_OUTPUT)


def assert_conversions(fn):
    assert_result("conversions", trace_conversions(fn))
