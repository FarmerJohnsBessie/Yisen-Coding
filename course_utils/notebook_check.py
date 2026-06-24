from __future__ import annotations

import importlib
from contextlib import redirect_stdout
from io import StringIO
from typing import Any, Callable, Iterable, NamedTuple


# Shared result objects. Normal function checks and trace checks both return this
# shape, so decorators, pytest assertions, and notebook printing stay consistent.
class CaseCheck(NamedTuple):
    label: str
    status: str
    detail: str = ""


class CaseResult(NamedTuple):
    passed: int
    total: int
    failures: list[str]
    checks: tuple[CaseCheck, ...] = ()
    kind: str = "check"


# Normal function checks.
def run_cases(
    fn: Callable[..., Any],
    cases: Iterable[tuple[str, tuple[Any, ...], Any]],
) -> CaseResult:
    failures: list[str] = []
    checks: list[CaseCheck] = []
    total = 0

    for label, args, expected in cases:
        total += 1

        try:
            actual = fn(*args)
        except Exception as exc:  # noqa: BLE001 - show beginner-friendly feedback
            detail = f"raised {type(exc).__name__}: {exc}"
            failures.append(f"{label}: {detail}")
            checks.append(CaseCheck(label=label, status="RE", detail=detail))
            continue

        if actual != expected:
            detail = f"expected {expected!r}, got {actual!r}"
            failures.append(f"{label}: {detail}")
            checks.append(CaseCheck(label=label, status="WA", detail=detail))
        else:
            checks.append(CaseCheck(label=label, status="AC"))

    return CaseResult(
        passed=total - len(failures),
        total=total,
        failures=failures,
        checks=tuple(checks),
        kind="check",
    )


# Code-trace checks. Students write predicted output with print(...) lines, and
# this helper captures stdout so GitHub can grade the saved notebook source.
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
        detail = f"raised {type(exc).__name__}: {exc}"
        return CaseResult(
            passed=0,
            total=1,
            failures=[f"{label}: {detail}"],
            checks=(CaseCheck(label=label, status="RE", detail=detail),),
            kind="trace",
        )

    actual_text = normalize_trace_output(actual)
    expected_text = normalize_trace_output(expected)

    if actual_text != expected_text:
        detail = f"expected {expected_text!r}, got {actual_text!r}"
        return CaseResult(
            passed=0,
            total=1,
            failures=[f"{label}: {detail}"],
            checks=(CaseCheck(label=label, status="WA", detail=detail),),
            kind="trace",
        )

    return CaseResult(
        passed=1,
        total=1,
        failures=[],
        checks=(CaseCheck(label=label, status="AC"),),
        kind="trace",
    )


# Notebook display formatting.
def color(text: str, color_code: str) -> str:
    return f"\033[{color_code}m{text}\033[0m"


def color_status(status: str) -> str:
    colors = {
        "AC": "32;1",
        "WA": "31;1",
        "RE": "35;1",
        "PASS": "32;1",
        "FAIL": "31;1",
    }
    return color(status, colors.get(status, "0"))


def format_check_lines(result: CaseResult) -> list[str]:
    lines = []
    for index, check in enumerate(result.checks, start=1):
        if check.status == "AC":
            lines.append(f"{color_status('AC')}  Test case {index} passed")
        elif check.status == "WA":
            lines.append(
                f"{color_status('WA')}  Test case {index} failed: "
                f"{check.label} - {check.detail}"
            )
        elif check.status == "RE":
            lines.append(
                f"{color_status('RE')}  Test case {index} errored: "
                f"{check.label} - {check.detail}"
            )

    return lines


def format_trace_lines(result: CaseResult) -> list[str]:
    lines = []
    for check in result.checks:
        if check.status == "AC":
            lines.append(f"{color_status('AC')}  Trace passed")
        elif check.status == "WA":
            lines.append(f"{color_status('WA')}  Trace failed")
        elif check.status == "RE":
            lines.append(f"{color_status('RE')}  Trace errored: {check.detail}")

    return lines


def format_result(name: str, result: CaseResult) -> str:
    status = "PASS" if result.passed == result.total else "FAIL"
    lines = (
        format_trace_lines(result)
        if result.kind == "trace"
        else format_check_lines(result)
    )

    if not lines:
        lines.extend(f" - {failure}" for failure in result.failures)

    lines.append(
        f"[{color_status(status)}] {name}: {result.passed}/{result.total} tests passed"
    )
    return "\n".join(lines)


def print_result(name: str, result: CaseResult) -> None:
    print(format_result(name, result))


def assert_result(name: str, result: CaseResult) -> None:
    if result.failures:
        raise AssertionError(format_result(name, result))


# Notebook decorators.
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
