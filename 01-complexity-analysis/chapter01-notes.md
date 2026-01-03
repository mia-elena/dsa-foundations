# Chapter 1: Python Primer

**Purpose:** Foundational review of Python syntax and object-oriented model for those with prior programming experience.

---

## 1.1 Python Overview

### The Interpreter
- Python is an **interpreted language**
- Commands executed by the Python interpreter
- Two modes:
  - **Interactive mode:** For debugging and testing
  - **Script mode:** Execute `.py` files

### Syntax Basics

**Whitespace:**
- Statements typically end with newline
- **Indentation is critical** - delimits control structure bodies
```python
if x > 0:
    print("positive")  # Indentation matters!
    print("done")
```

**Comments:**
- Use `#` for human-readable annotations
```python
# This is a comment
x = 10  # Inline comment
```

---

## 1.2 Objects in Python

### Identifiers and Assignment
- **Case-sensitive** (e.g., `myVar` ≠ `myvar`)
- Cannot start with a numeral
- Assignment associates identifier with object in memory
```python
x = 10.5  # x now references a float object
```

### Dynamic Typing
- Unlike Java/C++, Python is **dynamically typed**
- An identifier can reference any type and be reassigned
```python
x = 10      # x is an int
x = "hello" # now x is a string (totally valid!)
```

### Aliasing
- Multiple identifiers can reference the same object
```python
a = [1, 2, 3]
b = a  # b and a are aliases (point to same list)
```

### Built-in Classes

**Immutable Types** (cannot be changed after creation):
- `bool` - True/False
- `int` - arbitrary magnitude integers
- `float` - fixed-precision decimals
- `tuple` - immutable sequence
- `str` - strings
- `frozenset` - immutable set

**Mutable Types** (can be modified):
- `list` - mutable sequence
- `set` - unordered, no duplicates
- `dict` - key-value mapping

```python
# Immutable example
x = 5
x = x + 1  # Creates NEW int object, doesn't modify original

# Mutable example
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the SAME list object
```

---

## 1.3 Expressions, Operators, and Precedence

### Logical Operators
- `not` - negation
- `and` - logical AND (short-circuit)
- `or` - logical OR (short-circuit)

```python
x = True and False  # False
y = True or False   # True
```

### Equality vs. Identity
- `==` tests for **equivalent values**
- `is` tests for **same identity** (same object in memory)

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b  # True (same values)
a is b  # False (different objects)
a is c  # True (same object, aliases)
```

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `/` | True division (returns float) | `7 / 2` → `3.5` |
| `//` | Integer division (floor) | `7 // 2` → `3` |
| `%` | Modulo (remainder) | `7 % 2` → `1` |
| `**` | Exponentiation | `2 ** 3` → `8` |

### Sequence Operations
All sequence types support:
- **Indexing:** `s[j]` - access element at index j
- **Slicing:** `s[start:stop]` - subsequence
- **Containment:** `val in s` - check if val exists

```python
my_list = [10, 20, 30, 40, 50]
my_list[2]      # 30
my_list[1:4]    # [20, 30, 40]
30 in my_list   # True
```

---

## 1.4 Control Flow

### Conditionals
```python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

### While Loops
Repeat while condition is True:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### For Loops
Iterate through iterable structures:
```python
for item in [1, 2, 3, 4]:
    print(item)
```

### Range
Built-in class for integer sequences:
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8 (step of 2)
```

---

## 1.5 Functions

### Function Definitions
```python
def square(n):
    """Returns the square of n."""
    return n * n
```

### Information Passing
- Parameters passed using **assignment semantics**
- **Mutable parameters** (lists, dicts) can be modified in function
```python
def modify_list(lst):
    lst.append(100)  # Modifies original list!

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 100]
```

### Polymorphism
- **Default parameters:** `def greet(name="World"):`
- **Keyword arguments:** `greet(name="Alice")`

```python
def power(base, exponent=2):
    return base ** exponent

power(3)        # 9 (uses default exponent=2)
power(3, 3)     # 27
power(base=2, exponent=4)  # 16 (keyword args)
```

---

## 1.6 Simple Input and Output

### Console I/O
```python
# Output
print("Hello", "World", sep="-", end="!\n")  # Hello-World!

# Input
name = input("Enter your name: ")  # Returns string
age = int(input("Enter age: "))    # Convert to int
```

### File I/O
```python
# Writing
f = open("data.txt", "w")  # 'w' = write (overwrite)
f.write("Hello, file!")
f.close()

# Reading
f = open("data.txt", "r")  # 'r' = read
content = f.read()
f.close()

# Appending
f = open("data.txt", "a")  # 'a' = append
f.write("\nNew line")
f.close()
```

**Common modes:**
- `'r'` - read
- `'w'` - write (overwrite)
- `'a'` - append

---

## 1.7 Exception Handling

### Python Philosophy
"It is easier to ask for forgiveness than it is to get permission"

Use `try-except` blocks to handle errors gracefully:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Common Exception Types

| Exception | When it occurs |
|-----------|----------------|
| `IndexError` | Invalid sequence index |
| `KeyError` | Nonexistent dictionary key |
| `ValueError` | Invalid parameter value |
| `TypeError` | Wrong parameter type |

```python
# Example with multiple exceptions
try:
    data = [1, 2, 3]
    print(data[10])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Invalid value")
```

---

## 1.8 Iterators and Generators

### Iterators
Objects that manage a series of values:
```python
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator) would raise StopIteration
```

### Generators
Create iterators using `yield` instead of `return`:
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)  # Prints 1, 2, 3, 4, 5
```

**Key benefit:** **Lazy evaluation** - values computed only when needed (memory efficient!)

---

## 1.9 Python Conveniences

### Comprehensions
Concise syntax for creating collections:

**List comprehension:**
```python
squares = [k*k for k in range(1, 6)]  # [1, 4, 9, 16, 25]
```

**Set comprehension:**
```python
unique_squares = {k*k for k in [1, -1, 2, -2]}  # {1, 4}
```

**Dictionary comprehension:**
```python
square_dict = {k: k*k for k in range(1, 6)}  # {1:1, 2:4, 3:9, 4:16, 5:25}
```

**With conditions:**
```python
evens = [k for k in range(10) if k % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Unpacking
Assign multiple variables at once:
```python
a, b = 10, 20  # a=10, b=20
x, y, z = [1, 2, 3]

# Swap values
a, b = b, a
```

---

## 1.10 Scopes and Namespaces

### Namespaces
Abstractions that manage identifiers in a given scope:
- **Local scope:** Inside a function
- **Global scope:** Module level
- **Built-in scope:** Python's built-in names

```python
x = 10  # Global

def my_function():
    x = 5  # Local (shadows global)
    print(x)  # Prints 5

my_function()
print(x)  # Prints 10 (global unchanged)
```

### First-Class Objects
Functions and classes are **first-class objects** in Python:
- Can be assigned to variables
- Can be passed as parameters
- Can be returned from functions

```python
def square(n):
    return n * n

f = square  # Assign function to variable
print(f(5))  # 25

def apply_function(func, value):
    return func(value)

result = apply_function(square, 4)  # 16
```

---

## Key Takeaways

1. Python is dynamically typed and uses indentation for structure
2. Understand mutability vs. immutability
3. Know the difference between `==` (value equality) and `is` (identity)
4. Use exception handling for robust code
5. Leverage comprehensions for concise, readable code
6. Functions are first-class objects in Python
