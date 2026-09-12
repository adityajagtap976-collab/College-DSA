"""A singly linked list with insertion and deletion."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    value: T
    next: _Node[T] | None = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self._head: _Node[T] | None = None
        self._size = 0

    def append(self, value: T) -> None:
        node = _Node(value)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def prepend(self, value: T) -> None:
        self._head = _Node(value, self._head)
        self._size += 1

    def delete(self, value: T) -> None:
        previous: _Node[T] | None = None
        current = self._head
        while current is not None and current.value != value:
            previous, current = current, current.next
        if current is None:
            raise ValueError(f"value not found: {value!r}")
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next
        self._size -= 1

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def to_list(self) -> list[T]:
        return list(self)
