"""
Python Built-in Classes Examples
Chapter 1: Python Primer

Demonstrates all built-in classes mentioned in the textbook:
- Immutable: bool, int, float, tuple, str, frozenset
- Mutable: list, set, dict
"""

print("=" * 60)
print("IMMUTABLE TYPES - Cannot be changed after creation")
print("=" * 60)

# ============================================================
# 1. BOOL - Boolean values
# ============================================================
print("\n1. BOOL (Boolean)")
print("-" * 40)

is_student = True
is_graduated = False

print(f"is_student: {is_student}")
print(f"is_graduated: {is_graduated}")

# Boolean operations
print(f"not is_student: {not is_student}")
print(f"is_student and is_graduated: {is_student and is_graduated}")
print(f"is_student or is_graduated: {is_student or is_graduated}")

# Comparison results are bools
age = 20
print(f"age > 18: {age > 18}")
print(f"age == 21: {age == 21}")

# ============================================================
# 2. INT - Arbitrary magnitude integers
# ============================================================
print("\n2. INT (Integer)")
print("-" * 40)

small_int = 42
large_int = 123456789012345678901234567890  # Python handles huge integers!
negative_int = -17

print(f"small_int: {small_int}")
print(f"large_int: {large_int}")
print(f"negative_int: {negative_int}")

# Integer operations
print(f"10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"10 * 5 = {10 * 5}")
print(f"10 ** 3 = {10 ** 3}")  # Exponentiation
print(f"7 // 2 = {7 // 2}")    # Integer division
print(f"7 % 2 = {7 % 2}")      # Modulo

# ============================================================
# 3. FLOAT - Fixed-precision floating point
# ============================================================
print("\n3. FLOAT (Floating Point)")
print("-" * 40)

pi = 3.14159
temperature = -40.5
scientific = 1.23e-4  # Scientific notation

print(f"pi: {pi}")
print(f"temperature: {temperature}")
print(f"scientific notation: {scientific}")

# Float operations
print(f"7 / 2 = {7 / 2}")      # True division (returns float)
print(f"3.5 * 2 = {3.5 * 2}")
print(f"Round pi to 2 places: {round(pi, 2)}")

# ============================================================
# 4. TUPLE - Immutable sequence
# ============================================================
print("\n4. TUPLE (Immutable Sequence)")
print("-" * 40)

empty_tuple = ()
single_tuple = (42,)  # Note the comma!
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed_tuple = (1, "hello", 3.14, True)

print(f"empty_tuple: {empty_tuple}")
print(f"single_tuple: {single_tuple}")
print(f"coordinates: {coordinates}")
print(f"rgb_color: {rgb_color}")
print(f"mixed_tuple: {mixed_tuple}")

# Tuple operations
print(f"coordinates[0]: {coordinates[0]}")  # Indexing
print(f"rgb_color[1:3]: {rgb_color[1:3]}")  # Slicing
print(f"len(rgb_color): {len(rgb_color)}")  # Length
print(f"128 in rgb_color: {128 in rgb_color}")  # Containment

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# Tuples are immutable - this would error:
# coordinates[0] = 5  # TypeError!

# ============================================================
# 5. STR - String (immutable sequence of characters)
# ============================================================
print("\n5. STR (String)")
print("-" * 40)

greeting = "Hello"
name = 'Alice'
multiline = """This is a
multiline string"""
empty_str = ""

print(f"greeting: {greeting}")
print(f"name: {name}")
print(f"multiline: {multiline}")

# String operations
print(f"greeting + ' ' + name: {greeting + ' ' + name}")  # Concatenation
print(f"greeting * 3: {greeting * 3}")  # Repetition
print(f"greeting[0]: {greeting[0]}")    # Indexing
print(f"greeting[1:4]: {greeting[1:4]}")  # Slicing
print(f"len(greeting): {len(greeting)}")
print(f"'H' in greeting: {'H' in greeting}")

# String methods
print(f"greeting.upper(): {greeting.upper()}")
print(f"greeting.lower(): {greeting.lower()}")
print(f"'hello world'.split(): {'hello world'.split()}")
print(f"'-'.join(['a','b','c']): {'-'.join(['a','b','c'])}")

# Strings are immutable - this would error:
# greeting[0] = 'h'  # TypeError!

# ============================================================
# 6. FROZENSET - Immutable set
# ============================================================
print("\n6. FROZENSET (Immutable Set)")
print("-" * 40)

frozen_nums = frozenset([1, 2, 3, 4, 4])  # Duplicates removed
frozen_colors = frozenset(['red', 'green', 'blue'])

print(f"frozen_nums: {frozen_nums}")
print(f"frozen_colors: {frozen_colors}")

# Frozenset operations
print(f"3 in frozen_nums: {3 in frozen_nums}")
print(f"len(frozen_nums): {len(frozen_nums)}")

# Set operations (mathematical)
set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])
print(f"set_a union set_b: {set_a | set_b}")
print(f"set_a intersection set_b: {set_a & set_b}")
print(f"set_a difference set_b: {set_a - set_b}")

# Frozensets are immutable - no add/remove methods

print("\n" + "=" * 60)
print("MUTABLE TYPES - Can be modified after creation")
print("=" * 60)

# ============================================================
# 7. LIST - Mutable sequence
# ============================================================
print("\n7. LIST (Mutable Sequence)")
print("-" * 40)

empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"empty_list: {empty_list}")
print(f"numbers: {numbers}")
print(f"mixed_list: {mixed_list}")
print(f"nested_list: {nested_list}")

# List operations (similar to tuples)
print(f"numbers[0]: {numbers[0]}")        # Indexing
print(f"numbers[1:4]: {numbers[1:4]}")    # Slicing
print(f"numbers[-1]: {numbers[-1]}")      # Negative indexing
print(f"3 in numbers: {3 in numbers}")    # Containment
print(f"len(numbers): {len(numbers)}")

# Lists are MUTABLE - can be modified
numbers[0] = 100
print(f"After numbers[0] = 100: {numbers}")

numbers.append(6)
print(f"After append(6): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

numbers.remove(100)
print(f"After remove(100): {numbers}")

popped = numbers.pop()
print(f"After pop(): {numbers}, popped value: {popped}")

numbers.extend([7, 8, 9])
print(f"After extend([7,8,9]): {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

numbers.reverse()
print(f"After reverse(): {numbers}")

# ============================================================
# 8. SET - Mutable unordered collection (no duplicates)
# ============================================================
print("\n8. SET (Mutable Unordered Collection)")
print("-" * 40)

empty_set = set()  # Note: {} creates a dict, not a set!
unique_nums = {1, 2, 3, 4, 4, 4}  # Duplicates removed
colors = {'red', 'green', 'blue'}

print(f"empty_set: {empty_set}")
print(f"unique_nums: {unique_nums}")  # Only one 4
print(f"colors: {colors}")

# Set operations
print(f"3 in unique_nums: {3 in unique_nums}")
print(f"len(colors): {len(colors)}")

# Sets are MUTABLE - can be modified
colors.add('yellow')
print(f"After add('yellow'): {colors}")

colors.remove('red')  # Raises KeyError if not found
print(f"After remove('red'): {colors}")

colors.discard('purple')  # No error if not found
print(f"After discard('purple'): {colors}")

# Mathematical set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"Union (set1 | set2): {set1 | set2}")
print(f"Intersection (set1 & set2): {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric difference (set1 ^ set2): {set1 ^ set2}")

# ============================================================
# 9. DICT - Mutable associative mapping (key-value pairs)
# ============================================================
print("\n9. DICT (Dictionary - Key-Value Mapping)")
print("-" * 40)

empty_dict = {}
student = {
    'name': 'Alice',
    'age': 20,
    'gpa': 3.8,
    'courses': ['CS101', 'MATH201']
}
grades = {'A': 4.0, 'B': 3.0, 'C': 2.0}

print(f"empty_dict: {empty_dict}")
print(f"student: {student}")
print(f"grades: {grades}")

# Dictionary operations
print(f"student['name']: {student['name']}")  # Access by key
print(f"grades['A']: {grades['A']}")
print(f"'age' in student: {'age' in student}")  # Check key existence
print(f"len(student): {len(student)}")

# Dictionaries are MUTABLE - can be modified
student['major'] = 'Computer Science'
print(f"After adding 'major': {student}")

student['age'] = 21
print(f"After updating 'age': {student}")

del student['gpa']
print(f"After deleting 'gpa': {student}")

# Dictionary methods
print(f"student.keys(): {student.keys()}")
print(f"student.values(): {student.values()}")
print(f"student.items(): {student.items()}")

print(f"student.get('major'): {student.get('major')}")
print(f"student.get('gpa', 0.0): {student.get('gpa', 0.0)}")  # Default value

# Iterating through dictionary
print("\nIterating through student dict:")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================================
# DEMONSTRATING MUTABILITY vs IMMUTABILITY
# ============================================================
print("\n" + "=" * 60)
print("MUTABILITY vs IMMUTABILITY DEMONSTRATION")
print("=" * 60)

# Immutable example (int)
print("\nImmutable (int):")
x = 10
y = x  # y references the same object as x
print(f"x = {x}, y = {y}")
x = x + 1  # Creates NEW int object
print(f"After x = x + 1:")
print(f"x = {x}, y = {y}")  # y unchanged!

# Mutable example (list)
print("\nMutable (list):")
list1 = [1, 2, 3]
list2 = list1  # list2 is an ALIAS of list1
print(f"list1 = {list1}, list2 = {list2}")
list1.append(4)  # Modifies the SAME list
print(f"After list1.append(4):")
print(f"list1 = {list1}, list2 = {list2}")  # Both changed!

# To copy a list instead of aliasing:
list3 = [1, 2, 3]
list4 = list3.copy()  # or list3[:]
list3.append(4)
print(f"\nWith copy:")
print(f"list3 = {list3}, list4 = {list4}")  # list4 unchanged

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
