# Lesson 3: Data Structures Cheatsheet

A quick reference guide for Lists, Tuples, Sets, and Dictionaries in Python.

## Core Concepts & Built-ins
No external libraries are required. All structures and functions are built directly into Python.

*   `list`: Ordered, mutable collection. `[1, 2, 3]`
*   `tuple`: Ordered, immutable collection. `(1, 2, 3)`
*   `set`: Unordered, mutable collection of unique items. `{1, 2, 3}`
*   `dict`: Collection of key-value pairs. `{"key": "value"}`

---

## 1. Lists (`list`)
An ordered collection of items that is **mutable** (can be changed).

```python
# Creation
fruits = ["apple", "banana", "cherry"]

# Slicing (same as string slicing)
print(fruits[0])      # "apple"
print(fruits[-1])     # "cherry" (last element)
print(fruits[0:2])    # ["apple", "banana"] (index 2 is excluded)

# Common Methods
fruits.append("date") # Adds to the end -> ["apple", "banana", "cherry", "date"]
fruits.insert(1, "fig")# Inserts at index 1 -> ["apple", "fig", "banana", ...]
fruits.remove("banana")# Removes first occurrence of "banana"
popped = fruits.pop() # Removes and returns the last item
fruits.sort()         # Sorts list alphabetically or numerically
```

---

## 2. Tuples (`tuple`)
An ordered collection of items that is **immutable** (cannot be changed once created). Very useful for read-only data.

```python
# Creation (note the parentheses)
coordinates = (10, 20)

# Accessing
print(coordinates[0])  # 10

# Immutable behavior
# coordinates[0] = 5   # ❌ TypeError: 'tuple' object does not support item assignment

# Methods (Tuples have only 2 built-in methods!)
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # 2 (counts occurrences of value 2)
print(my_tuple.index(3))  # 3 (finds index of value 3)
```

---

## 3. Sets (`set`)
An unordered collection of **unique** items. Sets do not allow duplicates and are mutable.

```python
# Creation (note the curly braces, but no key-value pairs)
my_set = {1, 2, 3, 3, 4}
print(my_set)  # {1, 2, 3, 4} (duplicates are automatically removed!)

# Adding & Removing
my_set.add(5)
my_set.discard(3)  # Removes 3. (discard won't throw an error if 3 is missing)

# Set Mathematical Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))        # {1, 2, 3, 4, 5} (All unique elements from both)
print(set_a.intersection(set_b)) # {3} (Elements present in both sets)
print(set_a.difference(set_b))   # {1, 2} (Elements in set_a but not in set_b)
```

---

## 4. Dictionaries (`dict`)
An unordered (as of Python 3.7+, ordered by insertion), mutable collection of **key-value pairs**.

```python
# Creation
user = {
    "name": "Krish",
    "role": "Trainer",
    "topic": "Deep Learning"
}

# Accessing values
print(user["name"])               # "Krish"
print(user.get("age", "N/A"))     # "N/A" (Safely gets value, returns default if missing)

# Adding or Updating
user["age"] = 32                  # Adds "age": 32
user["role"] = "Senior Trainer"   # Updates "role"

# Getting keys and values
print(list(user.keys()))          # ["name", "role", "topic", "age"]
print(list(user.values()))        # ["Krish", "Senior Trainer", ...]
print(list(user.items()))         # [("name", "Krish"), ("role", "Senior Trainer"), ...]

# Loop through a dictionary
for key, value in user.items():
    print(f"{key}: {value}")
```
