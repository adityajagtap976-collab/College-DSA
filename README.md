
# DSA College

A professional, testable Python implementation of common data structures and algorithms.

## Included

- Linear and binary search
- Bubble, insertion, quick, and merge sort
- Set union, intersection, difference, and symmetric difference
- LIFO stack with `push` and `pop`
- Infix-to-postfix conversion and postfix evaluation
- List-backed and fixed-capacity circular queues
- Singly linked list with append, prepend, and delete

## Run

Install the project and development tools with [uv](https://docs.astral.sh/uv/):

```powershell
uv sync
uv run pytest
uv run dsa-demo
```

The reusable implementations live directly in `src`; tests are in `tests`.
