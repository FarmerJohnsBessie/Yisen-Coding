from __future__ import annotations

import importlib
from contextlib import redirect_stdout
from io import StringIO
from typing import Any, Callable, Iterable, NamedTuple


class CaseResult(NamedTuple):
    passed: int
    total: int
    failures: list[str]


def run_cases(
    fn: Callable[..., Any],
    cases: Iterable[tuple[str, tuple[Any, ...], Any]],
) -> CaseResult:
    failures: list[str] = []
    total = 0

    for label, args, expected in cases:
        total += 1

        try:
            actual = fn(*args)
        except Exception as exc:  # noqa: BLE001 - show beginner-friendly feedback
            failures.append(f"{label}: raised {type(exc).__name__}: {exc}")
            continue

        if actual != expected:
            failures.append(f"{label}: expected {expected!r}, got {actual!r}")

    return CaseResult(passed=total - len(failures), total=total, failures=failures)


def normalize_trace_output(value: Any) -> str:
    """Normalize beginner trace answers without caring about line indentation."""

    if value is None:
        return ""

    if isinstance(value, (list, tuple)):
        return "\n".join(str(line).strip() for line in value)

    return "\n".join(line.strip() for line in str(value).strip().splitlines())


def capture_trace_output(fn: Callable[[], Any]) -> Any:
    output = StringIO()

    with redirect_stdout(output):
        returned = fn()

    printed = output.getvalue()
    return printed if printed else returned


def run_traces(
    fn: Callable[[], Any],
    expected: Any,
) -> CaseResult:
    label = f"{fn.__name__}()"

    try:
        actual = capture_trace_output(fn)
    except Exception as exc:  # noqa: BLE001 - show beginner-friendly feedback
        return CaseResult(
            passed=0,
            total=1,
            failures=[f"{label}: raised {type(exc).__name__}: {exc}"],
        )

    actual_text = normalize_trace_output(actual)
    expected_text = normalize_trace_output(expected)

    if actual_text != expected_text:
        return CaseResult(
            passed=0,
            total=1,
            failures=[f"{label}: expected {expected_text!r}, got {actual_text!r}"],
        )

    return CaseResult(passed=1, total=1, failures=[])


def format_result(name: str, result: CaseResult) -> str:
    status = "PASS" if result.passed == result.total else "FAIL"
    lines = [f"[{status}] {name}: {result.passed}/{result.total} tests passed"]
    lines.extend(f" - {failure}" for failure in result.failures)
    return "\n".join(lines)


def print_result(name: str, result: CaseResult) -> None:
    print(format_result(name, result))


def assert_result(name: str, result: CaseResult) -> None:
    if result.failures:
        raise AssertionError(format_result(name, result))


def check(name: str, cases_module: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Run notebook feedback when a decorated function cell is executed."""

    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        module = importlib.import_module(cases_module)
        check_fn = getattr(module, f"check_{name}")
        print_result(name, check_fn(fn))
        return fn

    return decorator


def trace(name: str, traces_module: str) -> Callable[[Callable[[], Any]], Callable[[], Any]]:
    """Run notebook trace feedback when a decorated answer cell is executed."""

    def decorator(fn: Callable[[], Any]) -> Callable[[], Any]:
        module = importlib.import_module(traces_module)
        trace_fn = getattr(module, f"trace_{name}")
        print_result(name, trace_fn(fn))
        return fn

    return decorator
