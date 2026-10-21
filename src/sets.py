"""Set operations."""

from typing import TypeVar

T = TypeVar("T")


def set_operations[T](first: set[T], second: set[T]) -> dict[str, set[T]]:
    """Return common set operations for two sets."""
    return {
        "union": first | second,
        "intersection": first & second,
        "difference": first - second,
        "symmetric_difference": first ^ second,
    }
