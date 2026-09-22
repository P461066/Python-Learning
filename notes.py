# Python Notes - My Learning Journey
# Started: 08 September 2026

# ====================================
# TABLE OF CONTENTS
# ====================================
# DAY 1 - Variables, Strings, Booleans
# DAY 2 - Arithmetic & Comparison Operators
# DAY 3 - Logical Operators & De Morgan's Laws
# DAY 4 - If / Elif / Else
# DAY 5 - Input & Type Conversion
# DAY 6 - Loops (While / For)
# DAY 7 - Break & Continue
# DAY 8 - range()
# DAY 9 - Nested Loops
# DAY 10 - Functions (def)
# DAY 11 - Return Statement
# DAY 12 - Default Parameters
# DAY 13 - Lists: Basics
# DAY 14 - Lists: Accessing, Modifying & Looping
# DAY 15 - Lists: Methods

# ====================================
# 📅 DAY 1 - 08 September 2026
# ====================================

# --- 1. VARIABLES ---
# A variable stores data. Python detects the data type automatically.
age = 20
score = 2100

# Use snake_case for variable names.
# my score = 100   ❌ invalid
# my_score = 1000  ✅ valid

# --- 2. STRINGS (str) ---
text1 = "This is a sentence"
text2 = 'This is also a sentence'

# --- 3. BOOLEANS (bool) ---
# A boolean can only be True or False.
variable_true = True
variable_false = False

# Python is case-sensitive:
# true  ❌ wrong
# True  ✅ correct

# ====================================
# 📅 DAY 2 - 09 September 2026
# ====================================

# --- 4. ARITHMETIC OPERATORS ---
# + addition, - subtraction, * multiplication
# / division, % remainder, ** exponent

a = 2
b = 3
print(a + b)  # 5

# --- 5. AUGMENTED ASSIGNMENT ---
x = 10
x += 3    # 13
x -= 2    # 11
x *= 4    # 44
x /= 2    # 22.0
x %= 5    # 2.0

# --- 6. MODULUS (%) ---
remainder = 10 % 3  # 1
# number % 2 == 0 -> even
# number % 2 != 0 -> odd

# --- 7. COMPARISON OPERATORS ---
# == equal, != not equal, > greater than, < less than
# >= greater than or equal to, <= less than or equal to
print(1 == 1)  # True
print(1 != 2)  # True
print(1 < 2)   # True

# ====================================
# 📅 DAY 3 - 10 September 2026
# ====================================

# --- 8. LOGICAL OPERATORS ---
# and -> both conditions must be True
# or  -> at least one condition must be True
# not -> reverses a result

result1 = 13 > 12 and 12 < 13
result2 = 13 > 12 or 13 < 12
result3 = not (13 < 12)

# --- 9. DE MORGAN'S LAWS ---
# not (A and B) == (not A) or (not B)
# not (A or B)  == (not A) and (not B)

number = 15
result = not (number >= 1 and number <= 10)
print(result)  # True

# ====================================
# 📅 DAY 4 - 11 September 2026
# ====================================

# --- 10. IF / ELIF / ELSE ---
age = 20
if age > 18:
    status = "Adult"
else:
    status = "Child"
print(status)

score = 75
if score >= 90:
    grade = "A"
elif score >= 50:
    grade = "B"
else:
    grade = "C"
print(grade)

# --- 11. NESTED IF STATEMENTS ---
has_license = True
if age > 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")

# ====================================
# 📅 DAY 5 - 12 September 2026
# ====================================

# --- 12. INPUT() ---
# input() always returns a string.
# name = input("Enter your name: ")
# print("Hello " + name)

# --- 13. TYPE CONVERSION ---
# int() -> integer, float() -> decimal, str() -> string, bool() -> boolean
# age = int(input("Enter your age: "))
# price = float(input("Enter price: "))

# "5" + "5" = "55"
# 5 + 5 = 10

# ====================================
# 📅 DAY 6 - 13 September 2026
# ====================================

# --- 14. WHILE LOOP ---
count = 1
while count <= 5:
    print(count)
    count += 1

# --- 15. FOR LOOP ---
for number in range(5):
    print(number)  # 0, 1, 2, 3, 4

# ====================================
# 📅 DAY 7 - 14 September 2026
# ====================================

# --- 16. BREAK AND CONTINUE ---
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)  # odd numbers

for number in range(10):
    if number == 6:
        break
    print(number)  # 0 to 5

# ====================================
# 📅 DAY 8 - 15 September 2026
# ====================================

# --- 17. RANGE() ---
# range(stop) -> 0 through stop - 1
# range(start, stop) -> start through stop - 1
# range(start, stop, step) -> custom step

for number in range(5):
    print(number)
for number in range(2, 6):
    print(number)
for number in range(1, 10, 2):
    print(number)
for number in range(10, 0, -2):
    print(number)

# ====================================
# 📅 DAY 9 - 16 September 2026
# ====================================

# --- 18. NESTED LOOPS ---
for x in range(2):
    for y in range(2):
        print(x, y)

# Output: 0 0, 0 1, 1 0, 1 1
# The inner loop completes once for every outer-loop value.

# ====================================
# 📅 DAY 10 - 17 September 2026
# ====================================

# --- 19. FUNCTIONS (def) ---
# A function is a reusable block of code.

def greet(name):
    print(f"Hello {name}")

greet("Pablo")


def add(first_number, second_number):
    return first_number + second_number

print(add(5, 7))  # 12


def say_hello():
    print("Hello world")

say_hello()

# ====================================
# 📅 DAY 11 - 18 September 2026
# ====================================

# --- 20. RETURN STATEMENT ---
# return sends a value back and ends the function.

def add_numbers(first_number, second_number):
    return first_number + second_number

print(add_numbers(2, 3))  # 5


def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# print() displays a value. return gives a value back for reuse.

def with_print():
    print(10)


def with_return():
    return 10

x = with_print()   # None
y = with_return()  # 10
print(x)
print(y)

# ====================================
# 📅 DAY 12 - 19 September 2026
# ====================================

# --- 21. DEFAULT PARAMETERS ---
# A default parameter is used when no argument is supplied.

def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_with_default("Pablo"))
print(greet_with_default("Pablo", "Good morning"))

# Required parameters must come before default parameters.
# Correct:   def function(required_value, default_value="default"):
# Incorrect: def function(default_value="default", required_value):

# ====================================
# 📅 DAY 13 - 20 September 2026
# ====================================

# --- 22. LIST BASICS ---
# A list stores multiple values in square brackets.
# Lists are ordered, changeable, and indexed from 0.

fruits = ["apple", "banana", "orange"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", True, 3.6]
empty_list = []

print(fruits)
print(len(numbers))  # 4

# ====================================
# 📅 DAY 14 - 21 September 2026
# ====================================

# TOPIC: LISTS - ACCESSING, MODIFYING, AND LOOPING

# --- 23. ACCESSING LIST ITEMS ---
# Indexing starts at 0, not 1.

letters = ["a", "b", "c", "d", "e"]
print(letters[0])   # a: first item
print(letters[2])   # c: third item
print(letters[-1])  # e: last item

# The last item can also be accessed with:
# letters[len(letters) - 1]

# --- 24. MODIFYING LIST ITEMS ---
# Use an index to replace an item.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

# --- 25. LOOPING THROUGH A LIST ---
# Loop directly through the values when you do not need indexes.

for fruit in fruits:
    print(fruit)

# Use range(len(list)) when you need the index.
for index in range(len(fruits)):
    print(index, fruits[index])

# enumerate() is a cleaner way to get both the index and value.
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- 26. LIST LENGTH ---
# len() returns the number of items in a list.

print(len(fruits))  # 3

# ====================================
# DAY 14 SUMMARY
# ====================================

# - Lists store multiple values in one variable.
# - List indexes start at 0.
# - Use negative indexes to count from the end.
# - Use an index to change a list item.
# - len(list) returns the number of items.
# - Loop directly through values when indexes are unnecessary.
# - Use enumerate() when you need both indexes and values.

# ====================================
# 📅 DAY 15 - 22 September 2026
# ====================================

# --- 27. BASIC LIST METHODS ---
# These are common built-in methods for lists.

# append(element): adds an element to the end of the list
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# clear(): removes all elements from the list
numbers.clear()
print(numbers)  # []

# pop(index): removes and returns the element at the specified index
numbers = [10, 20, 30]
last_item = numbers.pop()
print(last_item)  # 30
print(numbers)    # [10, 20]

# reverse(): reverses the order of the list
letters = ["a", "b", "c"]
letters.reverse()
print(letters)  # ['c', 'b', 'a']

# sort(): sorts the list in ascending order
scores = [7, 3, 9, 1]
scores.sort()
print(scores)  # [1, 3, 7, 9]

# ====================================
# DAY 15 SUMMARY
# ====================================

# - append() adds a value to the end of a list.
# - clear() removes every item from the list.
# - pop() removes and returns an item by index.
# - reverse() flips the list order.
# - sort() arranges the list in ascending order.

# ====================================
# SAFE DEMO RUNNER
# ====================================


def _demo():
    demo_fruits = ["apple", "banana", "cherry"]
    print("List example:", demo_fruits)
    print("First item:", demo_fruits[0])
    print("List length:", len(demo_fruits))


if __name__ == "__main__":
    _demo()
