# First-Class Functions, Decorators, Logging

# First-Class Functions

def greet(name):
    return f"Hello, {name}"

# Assign function to variable
say_hello = greet
print(say_hello("Lohith"))

# Pass function as argument
def execute(func, value):
    return func(value)

print(execute(greet, "Python"))

# Decorators

def my_decorator(func):
    def wrapper():
        print("\nBefore function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def display():
    print("Inside function")

display()

# Logging

import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info("Dividing numbers")
    try:
        result = a / b
        logging.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error!")
        return None

divide(10, 2)
divide(10, 0)