import pytest

from src import (
    BinarySearchTree,
    ChainedHashTable,
    CircularLinkedList,
    CircularQueue,
    DoublyLinkedList,
    Graph,
    LinearProbingHashTable,
    LinkedList,
    ListQueue,
    MapADT,
    Matrix,
    QuadraticProbingHashTable,
    Stack,
    binary_search,
    bubble_sort,
    evaluate_postfix,
    heap_sort,
    infix_to_postfix,
    insertion_sort,
    linear_search,
    merge_sort,
    quick_sort,
    selection_sort,
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
    assert selection_sort(values.copy()) == [1, 2, 4, 5, 8]
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


def test_advanced_linked_lists() -> None:
    doubly = DoublyLinkedList[int]()
    doubly.append(2)
    doubly.prepend(1)
    doubly.delete(1)
    assert doubly.to_list() == [2]

    circular = CircularLinkedList[int]()
    for value in (1, 2, 3):
        circular.append(value)
    circular.delete(1)
    circular.delete(3)
    assert circular.to_list() == [2]


def test_hash_tables() -> None:
    for table in (
        ChainedHashTable(2),
        LinearProbingHashTable(3),
        QuadraticProbingHashTable(3),
    ):
        table.put("a", 1)
        table.put("b", 2)
        table.put("a", 3)
        assert table.get("a") == 3
        assert table.get("b") == 2

    mapping = MapADT[str, int]()
    mapping.put("answer", 42)
    assert mapping.get("answer") == 42
    matrix = Matrix[int](2, 2, 0)
    matrix[1, 0] = 7
    assert matrix.to_list() == [[0, 0], [7, 0]]


def test_trees_heaps_and_graphs() -> None:
    tree = BinarySearchTree[int]()
    for value in (4, 2, 6, 1, 3):
        tree.insert(value)
    assert tree.contains(3)
    assert not tree.contains(5)
    assert heap_sort([3, 1, 2]) == [1, 2, 3]

    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    assert graph.bfs(0) == [0, 1, 2, 3]
    assert graph.dfs(0) == [0, 1, 3, 2]
