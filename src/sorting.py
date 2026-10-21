"""Elementary and divide-and-conquer sorting algorithms."""

from collections.abc import MutableSequence
from typing import Any


def bubble_sort(items: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sort items in place with bubble sort and return the same sequence."""
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:
            break
    return items


def insertion_sort(items: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sort items in place with insertion sort and return the same sequence."""
    for index in range(1, len(items)):
        value = items[index]
        position = index - 1
        while position >= 0 and items[position] > value:
            items[position + 1] = items[position]
            position -= 1
        items[position + 1] = value
    return items


def selection_sort(items: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sort items in place with selection sort and return the same sequence."""
    for start in range(len(items) - 1):
        smallest = min(range(start, len(items)), key=items.__getitem__)
        if smallest != start:
            items[start], items[smallest] = items[smallest], items[start]
    return items


def quick_sort(items: list[Any]) -> list[Any]:
    """Return a new list sorted with quicksort."""
    if len(items) <= 1:
        return items.copy()
    pivot = items[len(items) // 2]
    lower = [item for item in items if item < pivot]
    equal = [item for item in items if item == pivot]
    higher = [item for item in items if item > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)


def merge_sort(items: list[Any]) -> list[Any]:
    """Return a new list sorted with merge sort."""
    if len(items) <= 1:
        return items.copy()
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    merged: list[Any] = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    return merged + left[left_index:] + right[right_index:]
