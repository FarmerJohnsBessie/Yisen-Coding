from course_utils.notebook_check import assert_result, run_traces


FIRST_PRINTS_OUTPUT = [
    "3",
    "10",
]


def trace_first_prints(fn):
    return run_traces(fn, FIRST_PRINTS_OUTPUT)


def assert_first_prints(fn):
    assert_result("first_prints", trace_first_prints(fn))


VARIABLE_UPDATE_OUTPUT = [
    "10",
    "5",
]


def trace_variable_update(fn):
    return run_traces(fn, VARIABLE_UPDATE_OUTPUT)


def assert_variable_update(fn):
    assert_result("variable_update", trace_variable_update(fn))
