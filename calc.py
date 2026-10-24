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
    a, op, b = text.split()
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations[op](float(a), float(b))


def average(numbers):
    """Return the mean of a list of numbers."""
    if not numbers:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)
