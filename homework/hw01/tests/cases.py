from course_utils.notebook_check import assert_result, run_cases


def check_double(fn):
    return run_cases(
        fn,
        [
            ("double(3)", (3,), 6),
            ("double(0)", (0,), 0),
            ("double(-4)", (-4,), -8),
            ("double(12)", (12,), 24),
            ("double(2.5)", (2.5,), 5.0),
        ],
    )


def assert_double(fn):
    assert_result("double", check_double(fn))


def check_rectangle_area(fn):
    return run_cases(
        fn,
        [
            ("rectangle_area(3, 4)", (3, 4), 12),
            ("rectangle_area(7, 2)", (7, 2), 14),
            ("rectangle_area(0, 5)", (0, 5), 0),
            ("rectangle_area(10, 10)", (10, 10), 100),
            ("rectangle_area(2.5, 4)", (2.5, 4), 10.0),
        ],
    )


def assert_rectangle_area(fn):
    assert_result("rectangle_area", check_rectangle_area(fn))


def check_average_score(fn):
    return run_cases(
        fn,
        [
            ("average_score(80, 100)", (80, 100), 90.0),
            ("average_score(70, 75)", (70, 75), 72.5),
            ("average_score(0, 10)", (0, 10), 5.0),
            ("average_score(100, 100)", (100, 100), 100.0),
            ("average_score(-2, 2)", (-2, 2), 0.0),
        ],
    )


def assert_average_score(fn):
    assert_result("average_score", check_average_score(fn))


def check_full_groups(fn):
    return run_cases(
        fn,
        [
            ("full_groups(23, 7)", (23, 7), 3),
            ("full_groups(12, 3)", (12, 3), 4),
            ("full_groups(5, 2)", (5, 2), 2),
            ("full_groups(0, 4)", (0, 4), 0),
            ("full_groups(99, 10)", (99, 10), 9),
        ],
    )


def assert_full_groups(fn):
    assert_result("full_groups", check_full_groups(fn))


def check_is_even(fn):
    return run_cases(
        fn,
        [
            ("is_even(4)", (4,), True),
            ("is_even(5)", (5,), False),
            ("is_even(0)", (0,), True),
            ("is_even(-2)", (-2,), True),
            ("is_even(101)", (101,), False),
        ],
    )


def assert_is_even(fn):
    assert_result("is_even", check_is_even(fn))


def check_total_seconds(fn):
    return run_cases(
        fn,
        [
            ("total_seconds(1, 2, 3)", (1, 2, 3), 3723),
            ("total_seconds(0, 5, 30)", (0, 5, 30), 330),
            ("total_seconds(2, 0, 0)", (2, 0, 0), 7200),
            ("total_seconds(0, 0, 45)", (0, 0, 45), 45),
            ("total_seconds(3, 10, 5)", (3, 10, 5), 11405),
        ],
    )


def assert_total_seconds(fn):
    assert_result("total_seconds", check_total_seconds(fn))


def check_can_enter_contest(fn):
    return run_cases(
        fn,
        [
            ("can_enter_contest(10, 80, True)", (10, 80, True), True),
            ("can_enter_contest(9, 90, True)", (9, 90, True), False),
            ("can_enter_contest(12, 79, True)", (12, 79, True), False),
            ("can_enter_contest(12, 85, False)", (12, 85, False), False),
            ("can_enter_contest(16, 100, True)", (16, 100, True), True),
        ],
    )


def assert_can_enter_contest(fn):
    assert_result("can_enter_contest", check_can_enter_contest(fn))
