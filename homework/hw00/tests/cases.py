from course_utils.notebook_check import assert_result, run_cases


def check_add_one(fn):
    return run_cases(
        fn,
        [
            ("add_one(0)", (0,), 1),
            ("add_one(1)", (1,), 2),
            ("add_one(5)", (5,), 6),
            ("add_one(-1)", (-1,), 0),
            ("add_one(100)", (100,), 101),
        ],
    )


def assert_add_one(fn):
    assert_result("add_one", check_add_one(fn))


def check_add_numbers(fn):
    return run_cases(
        fn,
        [
            ("add_numbers(2, 3)", (2, 3), 5),
            ("add_numbers(0, 0)", (0, 0), 0),
            ("add_numbers(-1, 1)", (-1, 1), 0),
            ("add_numbers(10, -4)", (10, -4), 6),
            ("add_numbers(100, 25)", (100, 25), 125),
        ],
    )


def assert_add_numbers(fn):
    assert_result("add_numbers", check_add_numbers(fn))
