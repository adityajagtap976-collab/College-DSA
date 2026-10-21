
# DSA College

A professional, testable Python implementation of common data structures and algorithms.

## Included

- Linear and binary search
- Bubble, insertion, quick, and merge sort
- Selection sort and heap sort
- One- and two-dimensional array and map ADTs
- Set union, intersection, difference, and symmetric difference
- Chained, linear-probing, and quadratic-probing hash tables
- LIFO stack with `push` and `pop`
- Infix-to-postfix conversion and postfix evaluation
- List-backed and fixed-capacity circular queues
- Singly, doubly, and circular linked lists
- Binary trees, binary search trees, and tree traversals
- Graph adjacency lists/matrices with BFS and DFS

## Run

Install the project and development tools with [uv](https://docs.astral.sh/uv/):

```powershell
uv sync
uv run pytest
uv run dsa-demo
```

The reusable implementations live directly in `src`; tests are in `tests`.
