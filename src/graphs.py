"""Graph representations and breadth/depth-first traversal."""

from collections import deque


class Graph:
    """Undirected graph represented by both an adjacency list and matrix."""

    def __init__(self, vertices: int) -> None:
        if vertices < 0:
            raise ValueError("vertices must be non-negative")
        self.adjacency_list: list[list[int]] = [[] for _ in range(vertices)]
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, first: int, second: int) -> None:
        self._validate(first)
        self._validate(second)
        if second not in self.adjacency_list[first]:
            self.adjacency_list[first].append(second)
            self.adjacency_list[second].append(first)
            self.adjacency_matrix[first][second] = 1
            self.adjacency_matrix[second][first] = 1

    def _validate(self, vertex: int) -> None:
        if not 0 <= vertex < len(self.adjacency_list):
            raise IndexError(f"invalid vertex: {vertex}")

    def bfs(self, start: int) -> list[int]:
        self._validate(start)
        visited = {start}
        queue = deque([start])
        order: list[int] = []
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: int) -> list[int]:
        self._validate(start)
        visited: set[int] = set()
        order: list[int] = []

        def visit(vertex: int) -> None:
            visited.add(vertex)
            order.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order
