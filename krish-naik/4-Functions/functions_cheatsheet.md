# Lesson 4: Functions Cheatsheet

A quick reference guide for defining functions, using arguments, lambdas, and higher-order functions like `map()` and `filter()`.

## Core Concepts & Built-ins
No external libraries are required. All structures are built directly into Python.

*   `def`: Keyword to define a function.
*   `return`: Keyword to exit a function and pass back a value.
*   `lambda`: Shortcut for creating small, anonymous functions.
*   `map(func, iterable)`: Applies a function to all items in an iterable.
*   `filter(func, iterable)`: Filters items from an iterable based on a condition function.

---

## 1. Defining Functions & Arguments
Functions allow you to reuse code blocks by giving them a name.

```python
# Simple definition with a parameter and default value
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Krish"))                  # "Hello, Krish!" (uses default message)
print(greet("Krish", message="Welcome")) # "Welcome, Krish!" (keyword argument)
```

### Variable-Length Arguments (`*args` and `**kwargs`)
*   **`*args`**: Receives positional arguments as a **tuple**. Use when you don't know how many numbers/arguments will be passed.
*   **`**kwargs`**: Receives keyword arguments as a **dictionary**.

```python
# *args example
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # 10

# **kwargs example
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Krish", role="Trainer", level="Expert")
# Outputs:
# name: Krish
# role: Trainer
# level: Expert
```

---

## 2. Lambda Functions
Lambdas are one-line, anonymous functions. They are useful for quick operations, especially when passed as arguments to other functions.

```python
# Traditional Function
def square(x):
    return x ** 2

# Lambda Function (equivalent)
square_lambda = lambda x: x ** 2

print(square_lambda(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7
```

---

## 3. Higher-Order Functions (`map` and `filter`)
These functions take other functions as arguments. They are usually combined with `lambda` expressions.

### Map Function
Applies a transformation function to every item in a list.

```python
numbers = [1, 2, 3, 4]

# Double each number using map
doubled = map(lambda x: x * 2, numbers)

# Note: map returns a map object, cast to list to see values
print(list(doubled))  # [2, 4, 6, 8]
```

### Filter Function
Passes each element through a function that returns a boolean (`True` or `False`), keeping only the elements that return `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # [2, 4, 6]
```
