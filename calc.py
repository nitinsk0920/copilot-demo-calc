"""A tiny calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def parse_expression(text):
    """Evaluate expressions like "6 / 3"."""
    a, op, b = text.split()
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations[op](float(a), float(b))
