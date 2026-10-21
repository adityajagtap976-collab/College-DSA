"""Doubly and circular linked lists."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


@dataclass
class _Node[T]:
    value: T
    previous: _Node[T] | None = None
    next: _Node[T] | None = None


class DoublyLinkedList[T]:
    """Linked list with constant-time insertion at either end."""

    def __init__(self) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0

    def append(self, value: T) -> None:
        node = _Node(value, previous=self._tail)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def prepend(self, value: T) -> None:
        node = _Node(value, next=self._head)
        if self._head is None:
            self._tail = node
        else:
            self._head.previous = node
        self._head = node
        self._size += 1

    def delete(self, value: T) -> None:
        current = self._head
        while current is not None and current.value != value:
            current = current.next
        if current is None:
            raise ValueError(f"value not found: {value!r}")
        if current.previous is None:
            self._head = current.next
        else:
            current.previous.next = current.next
        if current.next is None:
            self._tail = current.previous
        else:
            current.next.previous = current.previous
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


class CircularLinkedList[T]:
    """Circular singly linked list whose tail points back to the head."""

    def __init__(self) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0

    def append(self, value: T) -> None:
        node = _Node(value)
        if self._head is None:
            self._head = self._tail = node
            node.next = node
        else:
            node.next = self._head
            self._tail.next = node  # type: ignore[union-attr]
            self._tail = node
        self._size += 1

    def delete(self, value: T) -> None:
        if self._head is None:
            raise ValueError(f"value not found: {value!r}")
        previous = self._tail
        current = self._head
        for _ in range(self._size):
            if current.value == value:
                if self._size == 1:
                    self._head = self._tail = None
                else:
                    previous.next = current.next  # type: ignore[union-attr]
                    if current is self._head:
                        self._head = current.next
                    if current is self._tail:
                        self._tail = previous
                self._size -= 1
                return
            previous, current = current, current.next  # type: ignore[assignment]
        raise ValueError(f"value not found: {value!r}")

    def __iter__(self) -> Iterator[T]:
        current = self._head
        for _ in range(self._size):
            yield current.value  # type: ignore[union-attr]
            current = current.next  # type: ignore[union-attr]

    def __len__(self) -> int:
        return self._size

    def to_list(self) -> list[T]:
        return list(self)
