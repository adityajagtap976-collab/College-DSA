"""Searching algorithms."""

from collections.abc import Sequence
from typing import Any


def linear_search(items: Sequence[Any], target: Any) -> int:
    """Return the first index of target, or -1 when it is absent."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(items: Sequence[Any], target: Any) -> int:
    """Return target's index in an ascending sorted sequence, or -1."""
    left, right = 0, len(items) - 1
    while left <= right:
        middle = (left + right) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
