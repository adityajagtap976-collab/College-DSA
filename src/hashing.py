"""Hash tables demonstrating separate chaining and probing."""

from typing import Any


class ChainedHashTable:
    """Hash table using buckets of key-value pairs (separate chaining)."""

    def __init__(self, capacity: int = 8) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._buckets: list[list[tuple[Any, Any]]] = [[] for _ in range(capacity)]

    def _bucket(self, key: Any) -> list[tuple[Any, Any]]:
        return self._buckets[hash(key) % len(self._buckets)]

    def put(self, key: Any, value: Any) -> None:
        bucket = self._bucket(key)
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: Any) -> Any:
        for stored_key, value in self._bucket(key):
            if stored_key == key:
                return value
        raise KeyError(key)


class LinearProbingHashTable:
    """Fixed-capacity hash table using linear probing for collisions."""

    _EMPTY = object()

    def __init__(self, capacity: int = 8) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._slots: list[tuple[Any, Any] | object] = [self._EMPTY] * capacity

    def put(self, key: Any, value: Any) -> None:
        for offset in range(len(self._slots)):
            index = (hash(key) + offset) % len(self._slots)
            slot = self._slots[index]
            if slot is self._EMPTY or slot[0] == key:  # type: ignore[index]
                self._slots[index] = (key, value)
                return
        raise OverflowError("hash table is full")

    def get(self, key: Any) -> Any:
        for offset in range(len(self._slots)):
            slot = self._slots[(hash(key) + offset) % len(self._slots)]
            if slot is self._EMPTY:
                break
            if slot[0] == key:  # type: ignore[index]
                return slot[1]  # type: ignore[index]
        raise KeyError(key)


class QuadraticProbingHashTable(LinearProbingHashTable):
    """Fixed-capacity hash table using quadratic probing for collisions."""

    def put(self, key: Any, value: Any) -> None:
        for offset in range(len(self._slots)):
            index = (hash(key) + offset * offset) % len(self._slots)
            slot = self._slots[index]
            if slot is self._EMPTY or slot[0] == key:  # type: ignore[index]
                self._slots[index] = (key, value)
                return
        raise OverflowError("hash table is full")

    def get(self, key: Any) -> Any:
        for offset in range(len(self._slots)):
            slot = self._slots[(hash(key) + offset * offset) % len(self._slots)]
            if slot is self._EMPTY:
                break
            if slot[0] == key:  # type: ignore[index]
                return slot[1]  # type: ignore[index]
        raise KeyError(key)
