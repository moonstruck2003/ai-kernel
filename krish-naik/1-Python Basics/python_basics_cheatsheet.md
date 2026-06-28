# Lesson 1: Python Basics Cheatsheet

A quick reference guide for basic syntax, variables, datatypes, and operators in Python.

## Core Concepts & Built-ins
No external libraries are required for these basics. All functions used are built directly into Python.

*   `print()`: Outputs data to the console.
*   `type()`: Returns the data type of a variable.
*   `int()`, `float()`, `str()`, `bool()`: Built-in functions used for type casting (converting one type to another).

---

## 1. Syntax Rules
Python has clean, readable syntax rules that rely heavily on case sensitivity and formatting.

### Indentation
Python uses indentation (commonly 4 spaces or 1 tab) instead of curly braces `{}` to define code blocks (e.g., inside loops, functions, or conditionals).
```python
if True:
    print("This is inside the block")  # Correctly indented
print("This is outside the block")
```

### Case Sensitivity
Python is case-sensitive. Variable names `age` and `Age` are completely different.
```python
age = 25
Age = 30
print(age)  # Outputs: 25
print(Age)  # Outputs: 30
```

### Line Continuation & Multiple Statements
*   Use a backslash `\` to break a long statement across multiple lines.
*   Use a semicolon `;` to write multiple independent statements on a single line.
```python
# Line continuation
total = 10 + 20 + \
        30 + 40

# Multiple statements on one line
x = 5; y = 10; z = x + y
```

---

## 2. Variables & Type Inference
In Python, variables are dynamically typed. You don't need to declare their type beforehand; Python infers it at runtime.

```python
x = 10       # Re-assigning to different types is allowed
print(type(x))  # Outputs: <class 'int'>

x = "Hello"
print(type(x))  # Outputs: <class 'str'>
```

---

## 3. Data Types
The basic data types you'll use constantly in Python:

| Type | Description | Example |
| :--- | :--- | :--- |
| **Integer (`int`)** | Whole numbers (positive, negative, zero) | `age = 32` |
| **Float (`float`)** | Numbers with decimals | `pi = 3.14159` |
| **String (`str`)** | Text surrounded by single or double quotes | `name = "Krish"` |
| **Boolean (`bool`)**| Logical values representing truth | `is_active = True` |

### Type Casting (Conversion)
```python
# Convert float/string to integer
integer_val = int(3.9)       # Results in: 3 (decimals are truncated)
str_to_int = int("123")      # Results in: 123

# Convert int/string to float
float_val = float(10)        # Results in: 10.0

# Convert any type to string
string_val = str(45.67)      # Results in: "45.67"
```

---

## 4. Operators
Operators allow you to perform arithmetic, comparisons, and logical checks on data.

### Arithmetic Operators
```python
a = 10
b = 3

print(a + b)   # 13  (Addition)
print(a - b)   # 7   (Subtraction)
print(a * b)   # 30  (Multiplication)
print(a / b)   # 3.3333333333333335 (Float Division)
print(a // b)  # 3   (Floor Division - discards decimal part)
print(a % b)   # 1   (Modulus - returns remainder of division)
print(a ** b)  # 1000 (Exponentiation / Power: 10^3)
```

### Comparison Operators (Result is always a Boolean)
```python
x = 10
y = 20

print(x == y)  # False (Equal to)
print(x != y)  # True  (Not equal to)
print(x > y)   # False (Greater than)
print(x < y)   # True  (Less than)
print(x >= 10) # True  (Greater than or equal to)
```

### Logical Operators
Used to combine conditional statements.
```python
p = True
q = False

print(p and q) # False (Both must be True)
print(p or q)  # True  (At least one must be True)
print(not p)   # False (Inverts the value)
```
