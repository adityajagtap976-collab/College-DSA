"""Array and map ADTs built on Python's list and dictionary primitives."""

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Matrix[T]:
    """A fixed-size two-dimensional array with bounds checking."""

    def __init__(self, rows: int, columns: int, default: T) -> None:
        if rows < 0 or columns < 0:
            raise ValueError("matrix dimensions must be non-negative")
        self._data = [[default for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, position: tuple[int, int]) -> T:
        row, column = position
        return self._data[row][column]

    def __setitem__(self, position: tuple[int, int], value: T) -> None:
        row, column = position
        self._data[row][column] = value

    def to_list(self) -> list[list[T]]:
        return [row.copy() for row in self._data]


class MapADT[T, U]:
    """Small map ADT exposing insertion, lookup, deletion, and iteration."""

    def __init__(self) -> None:
        self._items: dict[T, U] = {}

    def put(self, key: T, value: U) -> None:
        self._items[key] = value

    def get(self, key: T) -> U:
        return self._items[key]

    def remove(self, key: T) -> U:
        return self._items.pop(key)

    def __contains__(self, key: T) -> bool:
        return key in self._items

    def __len__(self) -> int:
        return len(self._items)

    def items(self) -> Iterator[tuple[T, U]]:
        return iter(self._items.items())
