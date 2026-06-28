# Lesson 5: Modules and Packages Cheatsheet

A quick reference guide for importing built-in modules, using standard libraries, and structuring custom packages in Python.

## Core Concepts & Built-ins
No external libraries are required. Standard libraries are pre-installed with Python.

*   `import`: Imports an entire module or package.
*   `from ... import`: Imports specific functions, classes, or submodules.
*   `as`: Re-names an import with an alias for brevity.
*   `__init__.py`: Initializes a directory as a Python package.

---

## 1. Import Syntax
There are three primary ways to import code in Python:

```python
# 1. Import the whole module (requires using module prefix)
import math
print(math.sqrt(16))  # 4.0

# 2. Import specific items (no prefix needed)
from math import sqrt, pi
print(sqrt(9))        # 3.0
print(pi)             # 3.141592653589793

# 3. Import with an alias (rename for convenience)
import datetime as dt
print(dt.datetime.now())
```

---

## 2. Common Standard Libraries
Python comes with a rich standard library. Here are the most frequently used modules:

```python
# OS: File system navigation and environment interaction
import os
print(os.getcwd())               # Get current working directory
print(os.listdir("."))           # List files in the current folder

# SYS: Interpreter variables and system settings
import sys
print(sys.path)                  # List of directories Python searches for modules
print(sys.version)               # Python version info

# MATH: Mathematical operations
import math
print(math.factorial(5))         # 120

# RANDOM: Generate random values
import random
print(random.randint(1, 10))     # Random integer between 1 and 10
print(random.choice(["A", "B"])) # Picks random item from list

# DATETIME: Date and time tracking
from datetime import datetime
print(datetime.today().date())   # Current date
```

---

## 3. Creating Custom Packages & Subpackages
A **Module** is just a `.py` file. A **Package** is a folder containing modules and an `__init__.py` file.

### Folder Structure Example
To create a package, arrange your files like this:
```text
project/
│
├── main.py                    # Script running the imports
└── package/
    ├── __init__.py            # Marks folder as package (can be empty)
    ├── maths.py               # Module (e.g., defines addition)
    │
    └── subpackages/
        ├── __init__.py        # Marks sub-folder as package
        └── mult.py            # Submodule (e.g., defines multiplication)
```

### Importing Custom Packages
Assuming the files `maths.py` and `mult.py` contain custom math functions:

```python
# Importing from a package module
from package import maths
print(maths.addition(5, 3))

# Importing from a subpackage module
from package.subpackages import mult
print(mult.multiply(4, 2))
```
