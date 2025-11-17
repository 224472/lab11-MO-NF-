"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

# https://github.com/224472/lab11-MO-NF-
# Partner 1: [Michael Ou]
# Partner 2: [Partner finished with someone else]
def add(a, b): 
    return a+b
def sub(a, b): 
    return a - b
def mul(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a
def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)



