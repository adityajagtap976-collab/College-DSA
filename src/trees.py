"""Binary trees, binary search trees, and heaps."""

from __future__ import annotations

import heapq
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


@dataclass
class TreeNode[T]:
    value: T
    left: TreeNode[T] | None = None
    right: TreeNode[T] | None = None


def inorder[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def preorder[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def postorder[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


class BinarySearchTree[T]:
    def __init__(self) -> None:
        self.root: TreeNode[T] | None = None

    def insert(self, value: T) -> None:
        def add(node: TreeNode[T] | None) -> TreeNode[T]:
            if node is None:
                return TreeNode(value)
            if value < node.value:
                node.left = add(node.left)
            elif value > node.value:
                node.right = add(node.right)
            return node

        self.root = add(self.root)

    def contains(self, value: T) -> bool:
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False


def heap_sort[T](items: list[T]) -> list[T]:
    """Return items sorted using a binary min-heap."""
    heap = list(items)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]
