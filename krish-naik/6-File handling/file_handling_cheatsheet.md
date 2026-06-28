# Lesson 6: File Handling Cheatsheet

A quick reference guide for opening, reading, writing, appending files, and managing paths in Python.

## Core Concepts & Built-ins
No external libraries are required. File functions are built directly into Python; path manipulation utilizes the standard `os` library.

*   `open(filename, mode)`: Opens a file for standard operations.
*   `with`: Context manager that guarantees the file is safely closed when done.
*   `os.path`: Standard library submodule for path operations.

---

## 1. File Modes
When opening a file, you must specify the action mode:

| Mode | Name | Description |
| :--- | :--- | :--- |
| **`'r'`** | Read | Opens a file for reading. (Default. Errors if file doesn't exist). |
| **`'w'`** | Write | Opens a file for writing. (Overwrites existing content or creates new file). |
| **`'a'`** | Append | Opens a file to add content to the end. (Preserves existing content). |
| **`'b'`** | Binary | Opens file in binary mode (e.g., `'rb'` for images, `'wb'` for models). |

---

## 2. Reading and Writing Files

### Writing to a File
Always use the `with` statement! It acts as a safety wrapper so you never forget to close a file, preventing memory leaks.
```python
# Creates (or overwrites) 'example.txt' and writes text
with open('example.txt', 'w') as file:
    file.write("Hello World!\n")
    file.write("Welcome to Python file operations.")
```

### Appending to a File
```python
# Adds text to the end of the file without deleting current contents
with open('example.txt', 'a') as file:
    file.write("\nAdding this third line to the end.")
```

### Reading from a File
There are multiple ways to retrieve content from a file:
```python
# 1. read() - Reads the ENTIRE file as a single string
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 2. readline() - Reads a single line at a time
with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()

# 3. readlines() - Reads all lines into a list of strings
with open('example.txt', 'r') as file:
    lines_list = file.readlines()  # ["Hello World!\n", "Welcome..."]

# 4. Loop directly over file object (Memory-efficient for massive files)
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes trailing newlines \n
```

---

## 3. Path Operations (`os.path`)
Working with files often requires managing paths, file existence, and directories.

```python
import os

# 1. Join paths safely across OS differences (Windows uses \, Mac/Linux uses /)
path = os.path.join("data_folder", "sub_folder", "data.csv")
print(path)  # Windows output: data_folder\sub_folder\data.csv

# 2. Check if file or directory exists
print(os.path.exists("example.txt"))  # True/False
print(os.path.isfile("example.txt"))  # True (Checks if it is a file)
print(os.path.isdir("data_folder"))   # True (Checks if it is a directory)

# 3. Extract file information
full_path = "c:/Users/project/data.csv"
print(os.path.basename(full_path))    # "data.csv" (File name)
print(os.path.dirname(full_path))     # "c:/Users/project" (Directory name)
print(os.path.split(full_path))       # ('c:/Users/project', 'data.csv')
print(os.path.splitext(full_path))    # ('c:/Users/project/data', '.csv') (Splits extension)
```
