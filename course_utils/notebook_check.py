from __future__ import annotations

import importlib
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
