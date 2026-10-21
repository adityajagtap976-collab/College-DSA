"""List-backed and circular queues."""

from typing import TypeVar

T = TypeVar("T")


class ListQueue[T]:
    """FIFO queue backed by a list."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


class CircularQueue[T]:
    """Fixed-capacity FIFO queue that reuses freed slots."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._items: list[T | None] = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, item: T) -> None:
        if self.is_full():
            raise OverflowError("enqueue on full circular queue")
        position = (self._front + self._size) % len(self._items)
        self._items[position] = item
        self._size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from empty circular queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        return item  # type: ignore[return-value]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == len(self._items)

    def __len__(self) -> int:
        return self._size
