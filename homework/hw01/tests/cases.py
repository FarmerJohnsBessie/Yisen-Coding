from course_utils.notebook_check import assert_result, run_cases


def check_greet(fn):
    return run_cases(
        fn,
        [
            ("greet('Ada')", ("Ada",), "Hello, Ada!"),
            ("greet('Yisen')", ("Yisen",), "Hello, Yisen!"),
        ],
    )


def assert_greet(fn):
    assert_result("greet", check_greet(fn))


def check_add(fn):
    return run_cases(
        fn,
        [
            ("add(2, 3)", (2, 3), 5),
            ("add(-1, 1)", (-1, 1), 0),
            ("add(10, -4)", (10, -4), 6),
        ],
    )


def assert_add(fn):
    assert_result("add", check_add(fn))


def check_is_even(fn):
    return run_cases(
        fn,
        [
            ("is_even(4)", (4,), True),
            ("is_even(5)", (5,), False),
            ("is_even(0)", (0,), True),
        ],
    )


def assert_is_even(fn):
    assert_result("is_even", check_is_even(fn))
