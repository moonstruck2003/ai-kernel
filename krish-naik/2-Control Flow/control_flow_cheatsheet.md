# Lesson 2: Control Flow Cheatsheet

A quick reference guide for conditional statements, loops, and loop control statements in Python.

## Core Concepts & Built-ins
No external libraries are required. All syntax structures and helper functions are built directly into Python.

*   `if`, `elif`, `else`: Logical branching.
*   `for`, `while`: Loops for repetitive tasks.
*   `range()`: Generates a sequence of integers.
*   `enumerate()`: Yields index-item pairs from an iterable.
*   `zip()`: Pairs items from multiple iterables.

---

## 1. Conditional Statements
Used to execute blocks of code depending on whether a condition is `True` or `False`.

### If-Elif-Else Structure
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This block runs because 85 >= 80
else:
    print("Grade: C")
```

### Nested If Statement
```python
number = 10
if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive number")  # Prints this
else:
    print("Negative number")
```

---

## 2. Loops
Loops are used to repeat a block of code multiple times.

### For Loops (Iterable Iteration)
Use `for` loops when you know beforehand how many times you want to run the loop (e.g., iterating through a list or range).

```python
# Iterating over a string
for char in "NLP":
    print(char)  # Prints: N, then L, then P
```

#### Loop Helpers
*   **`range(start, stop, step)`**: Generates numbers. Stop is excluded.
```python
for i in range(1, 6, 2):
    print(i)  # Prints: 1, 3, 5
```
*   **`enumerate()`**: Loops through an iterable while keeping track of the index.
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # Prints: 0: apple, 1: banana...
```
*   **`zip()`**: Loops through multiple lists at the same time.
```python
names = ["Alice", "Bob"]
ages = [24, 27]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### While Loops (Condition-based Iteration)
Use `while` loops when you want to repeat a block of code until a specific condition becomes `False`.

```python
count = 1
while count <= 3:
    print(count)
    count += 1  # Increment to avoid an infinite loop!
```

---

## 3. Loop Control Statements
Used to change the normal execution flow of loops.

| Keyword | Description | Example |
| :--- | :--- | :--- |
| **`break`** | Stops the loop completely. | `if count == 5: break` |
| **`continue`** | Skips the rest of the current iteration and jumps to the next one. | `if i % 2 == 0: continue` |
| **`pass`** | A null statement. Used as a placeholder for future code. | `def future_function(): pass` |

### Code Examples
```python
# Break example: stop printing when you reach 'banana'
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        break
    print(fruit)  # Only prints: apple

# Continue example: skip even numbers
for num in range(1, 5):
    if num % 2 == 0:
        continue
    print(num)  # Only prints odd numbers: 1, 3
```
