from course_utils.notebook_check import assert_result, run_traces


BASICS_OUTPUT = [
    "0",
    "1",
    "71.9",
    "71",
]


def trace_basics(fn):
    return run_traces(fn, BASICS_OUTPUT)


def assert_basics(fn):
    assert_result("basics", trace_basics(fn))
