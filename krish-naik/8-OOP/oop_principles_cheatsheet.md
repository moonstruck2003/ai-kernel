# Lesson 8: Object-Oriented Programming (OOP) Cheatsheet

A comprehensive guide to Class creation, Inheritance, Polymorphism, Encapsulation, Abstraction, Magic Methods, and Operator Overloading in Python.

## Core Concepts & Built-ins
All OOP features are native. For abstraction, Python utilizes the standard library's `abc` module.

*   `class`: Keyword to define a class.
*   `__init__`: Constructor method, called when an object is instantiated.
*   `self`: Represents the specific instance of the class.
*   `super()`: Accesses parent class methods and constructors.
*   `abc.ABC`: Helper class to create Abstract Base Classes.

---

## 1. Classes, Objects, and Constructors
A **Class** is a blueprint; an **Object** is a concrete instance of that blueprint.

```python
class Car:
    # The Constructor
    def __init__(self, brand, color):
        self.brand = brand  # Instance attribute
        self.color = color  # Instance attribute

    # Instance Method
    def drive(self):
        return f"The {self.color} {self.brand} is driving!"

# Instantiate objects
car1 = Car("Tesla", "Red")
print(car1.drive())  # "The Red Tesla is driving!"
```

---

## 2. The 4 Pillars of OOP

### I. Inheritance
Allows a child class to inherit attributes and methods from a parent class, promoting code reusability.

```python
class Animal:
    def eat(self):
        return "Eating food"

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.eat())   # "Eating food" (inherited method)
print(my_dog.bark())  # "Woof!"
```

### II. Polymorphism
"Many forms." Different classes can define methods with the same name, allowing them to be called interchangeably.

```python
class Cat:
    def make_sound(self): return "Meow"

class Dog:
    def make_sound(self): return "Woof"

# Same method name, different behavior
for pet in [Cat(), Dog()]:
    print(pet.make_sound())  # Prints: Meow, then Woof
```

### III. Encapsulation
Restricting direct access to attributes and methods to prevent accidental modifications.
*   **Public**: `name` (accessible anywhere)
*   **Protected**: `_name` (accessible inside class & subclasses)
*   **Private**: `__name__` (accessible ONLY inside the class)

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self.__balance = balance    # Private (two underscores)

    # Getter method to access private data safely
    def get_balance(self):
        return self.__balance

account = BankAccount("Krish", 1000)
# print(account.__balance)  # ❌ AttributeError: Private variable!
print(account.get_balance()) # ✅ 1000
```

### IV. Abstraction
Hiding complex implementation details and showing only the essential features. Uses Abstract Base Classes (ABCs).

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Class
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        return "Kick-started bike engine!"  # Child MUST implement this

# my_vehicle = Vehicle()  # ❌ TypeError: Cannot instantiate abstract class!
my_bike = Bike()
print(my_bike.start_engine()) # ✅ "Kick-started bike engine!"
```

---

## 3. Magic (Dunder) Methods
Special methods prefixed and suffixed with double underscores `__`. They customize object behavior in Python.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Defines what is printed when print(object) is called
    def __str__(self):
        return f"'{self.title}' (Book)"

    # Defines what len(object) returns
    def __len__(self):
        return self.pages

book = Book("NLP Basics", 250)
print(book)      # Outputs: 'NLP Basics' (Book)
print(len(book)) # Outputs: 250
```

---

## 4. Operator Overloading
You can redefine how mathematical or comparison operators work on your custom objects by overriding specific magic methods.

*   `+` ➡️ `__add__`
*   `-` ➡️ `__sub__`
*   `*` ➡️ `__mul__`
*   `==` ➡️ `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the addition '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Under the hood, this calls p1.__add__(p2)
print(p3)     # Outputs: (4, 6)
```
