"""A tiny calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def parse_expression(text):
    """Evaluate expressions like "6 / 3"."""
    if not text.strip():
        raise ValueError("empty expression")
    a, op, b = text.split()
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations[op](float(a), float(b))
