import pytest

from src import (
    CircularQueue,
    LinkedList,
    ListQueue,
    Stack,
    binary_search,
    bubble_sort,
    evaluate_postfix,
    infix_to_postfix,
    insertion_sort,
    linear_search,
    merge_sort,
    quick_sort,
    set_operations,
)


def test_searching() -> None:
    assert linear_search([4, 2, 9, 2], 2) == 1
    assert linear_search([1, 2], 7) == -1
    assert binary_search([1, 2, 4, 8], 4) == 2
    assert binary_search([1, 2, 4, 8], 3) == -1


def test_sorting() -> None:
    values = [5, 1, 4, 2, 8]
    assert bubble_sort(values.copy()) == [1, 2, 4, 5, 8]
    assert insertion_sort(values.copy()) == [1, 2, 4, 5, 8]
    assert quick_sort(values) == [1, 2, 4, 5, 8]
    assert merge_sort(values) == [1, 2, 4, 5, 8]
    assert values == [5, 1, 4, 2, 8]


def test_sets_stack_and_expressions() -> None:
    assert set_operations({1, 2}, {2, 3}) == {
        "union": {1, 2, 3},
        "intersection": {2},
        "difference": {1},
        "symmetric_difference": {1, 3},
    }
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20 and stack.pop() == 20 and len(stack) == 1
    assert infix_to_postfix("3 + 4 * 2") == "3 4 2 * +"
    assert evaluate_postfix("3 4 2 * +") == 11


def test_queues_reuse_capacity() -> None:
    queue = ListQueue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    circular = CircularQueue[int](2)
    circular.enqueue(1)
    circular.enqueue(2)
    assert circular.dequeue() == 1
    circular.enqueue(3)
    assert circular.dequeue() == 2 and circular.dequeue() == 3
    with pytest.raises(OverflowError):
        circular.enqueue(4)
        circular.enqueue(5)
        circular.enqueue(6)


def test_linked_list_add_and_delete() -> None:
    linked = LinkedList[int]()
    linked.append(2)
    linked.prepend(1)
    linked.append(3)
    linked.delete(2)
    assert linked.to_list() == [1, 3]
    with pytest.raises(ValueError):
        linked.delete(9)
