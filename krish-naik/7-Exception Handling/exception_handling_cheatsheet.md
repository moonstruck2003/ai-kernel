# Lesson 7: Exception Handling Cheatsheet

A quick reference guide for catching, managing, and raising errors in Python to write robust code.

## Core Concepts & Built-ins
No external libraries are required. Error structures are built directly into Python.

*   `try`: Code block where exceptions/errors might occur.
*   `except`: Code block executed if a specific exception is raised.
*   `else`: Code block executed *only* if no exceptions were raised.
*   `finally`: Code block that *always* executes, regardless of whether an error occurred.
*   `raise`: Explicitly triggers an exception.

---

## 1. Try-Except Syntax
Instead of letting an error crash your entire program, you "catch" it and handle it gracefully.

```python
try:
    result = 10 / 0  # ❌ ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")  # Outputs: Error occurred: division by zero
```

---

## 2. Catching Multiple Specific Exceptions
You can catch different errors separately to respond to them in different ways.

```python
try:
    number = int("abc")  # ❌ ValueError: invalid literal for int()
    file = open("nonexistent.txt")  # ❌ FileNotFoundError
except ValueError:
    print("Please enter a valid number!")  # This will run
except FileNotFoundError:
    print("The requested file was not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # Catch-all for any other error
```

---

## 3. The `else` and `finally` Blocks
*   **`else`**: Runs only when the code inside the `try` block executes successfully without raising any exceptions.
*   **`finally`**: Runs no matter what. It is normally used for cleanup actions, like closing a database connection or closing a file, even if the program crashed.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully!")  # Runs if file exists
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File connection closed.")  # Runs no matter what!
```

---

## 4. Raising Exceptions
You can intentionally throw an error in your program when a condition isn't met using the `raise` keyword.

```python
def check_age(age):
    if age < 0:
        # Intentionally crash the function with a ValueError
        raise ValueError("Age cannot be a negative number!")
    return f"Age is {age}"

try:
    check_age(-5)
except ValueError as e:
    print(e)  # Outputs: Age cannot be a negative number!
```
