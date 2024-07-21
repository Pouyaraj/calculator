import math

def add(a, b):
    # Addition using Python's built-in operator
    return a + b

def subtract(a, b):
    # Subtraction using Python's built-in operator
    return a - b

def multiply(a, b):
    # Multiplication using Python's built-in operator
    return a * b

def divide(a, b):
    # Division using Python's built-in operator with error handling
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def square_root(a):
    # Square root calculation using math.sqrt
    return math.sqrt(a)

def sine(a):
    # Sine calculation using math.sin (convert degrees to radians)
    return math.sin(math.radians(a))

def cosine(a):
    # Cosine calculation using math.cos (convert degrees to radians)
    return math.cos(math.radians(a))

def round_result(value, decimals=10):
    # Rounding result to avoid floating-point precision issues
    return round(value, decimals)
