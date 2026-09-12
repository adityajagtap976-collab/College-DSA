"""Command-line demonstrations for the project."""

from .expressions import evaluate_postfix, infix_to_postfix
from .linked_list import LinkedList
from .queues import CircularQueue
from .searching import binary_search, linear_search
from .sets import set_operations
from .sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from .stack import Stack


def main() -> None:
    values = [7, 2, 9, 1, 5]
    print(f"Linear search for 9: index {linear_search(values, 9)}")
    sorted_values = merge_sort(values)
    print(f"Binary search for 5: index {binary_search(sorted_values, 5)}")
    print(f"Bubble sort: {bubble_sort(values.copy())}")
    print(f"Insertion sort: {insertion_sort(values.copy())}")
    print(f"Quick sort: {quick_sort(values)}")
    print(f"Merge sort: {sorted_values}")
    print(f"Set operations: {set_operations({1, 2}, {2, 3})}")

    stack = Stack[str]()
    stack.push("first")
    stack.push("last")
    print(f"Stack pop: {stack.pop()}")

    postfix = infix_to_postfix("3 + 4 * 2")
    print(f"Postfix: {postfix}; value: {evaluate_postfix(postfix)}")

    queue = CircularQueue[int](3)
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Circular queue dequeue: {queue.dequeue()}")

    linked = LinkedList[int]()
    linked.append(1)
    linked.append(2)
    linked.delete(1)
    print(f"Linked list after delete: {linked.to_list()}")


if __name__ == "__main__":
    main()
