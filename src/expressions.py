"""Infix/postfix expression conversion and evaluation."""

import operator
import re
from collections.abc import Callable

_OPERATORS: dict[str, tuple[int, Callable[[float, float], float]]] = {
    "+": (1, operator.add),
    "-": (1, operator.sub),
    "*": (2, operator.mul),
    "/": (2, operator.truediv),
    "^": (3, operator.pow),
}
_TOKEN = re.compile(r"\d+(?:\.\d+)?|[()+\-*/^]")


def infix_to_postfix(expression: str) -> str:
    """Convert a space-optional arithmetic expression to space-separated postfix."""
    tokens = _TOKEN.findall(expression.replace(" ", ""))
    if "".join(tokens) != expression.replace(" ", ""):
        raise ValueError("expression contains an unsupported token")
    output: list[str] = []
    operators: list[str] = []
    for token in tokens:
        if token[0].isdigit():
            output.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise ValueError("mismatched parentheses")
            operators.pop()
        else:
            while (
                operators
                and operators[-1] != "("
                and _OPERATORS[operators[-1]][0] >= _OPERATORS[token][0]
            ):
                output.append(operators.pop())
            operators.append(token)
    while operators:
        if operators[-1] == "(":
            raise ValueError("mismatched parentheses")
        output.append(operators.pop())
    return " ".join(output)


def evaluate_postfix(expression: str) -> float:
    """Evaluate a space-separated postfix expression containing binary operators."""
    values: list[float] = []
    for token in expression.split():
        if token not in _OPERATORS:
            try:
                values.append(float(token))
            except ValueError as error:
                raise ValueError(f"invalid postfix token: {token}") from error
            continue
        if len(values) < 2:
            raise ValueError("insufficient operands")
        right, left = values.pop(), values.pop()
        values.append(_OPERATORS[token][1](left, right))
    if len(values) != 1:
        raise ValueError("invalid postfix expression")
    return values[0]
