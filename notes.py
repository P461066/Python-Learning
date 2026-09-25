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
# DAY 16 - Tuples
# DAY 17 - enumerate() & String Methods
# CURRENT TOPIC - enumerate() & String Methods

# ====================================
# 📅 DAY 1 - 08 September 2026
# ====================================

# --- 1. VARIABLES ---
# A variable is a container that stores data.
# Python automatically detects the data type.

age = 20
score = 2100

# Tip:
# Variable names cannot contain spaces.
# Use snake_case instead.
# Example:
# my score = 100   ❌ invalid
# my_score = 1000  ✅ valid

# --- 2. STRING (str) ---
# A string stores text.
text1 = 'This is a sentence'
text2 = "This is also a sentence"

# Tip:
# Use single quotes or double quotes around text.

# --- 3. BOOLEAN (bool) ---
# A boolean only has two values: True or False.
variable_true = True
variable_false = False

# Tip:
# Python is case-sensitive.
# true  ❌ wrong
# True  ✅ correct

# ====================================
# 📅 DAY 2 - 09 September 2026
# ====================================

# --- 4. ARITHMETIC OPERATORS ---
# + addition
# - subtraction
# * multiplication
# / division
# % modulus (remainder)
# ** exponent

# Example:
a = 2
b = 3
c = a + b
print(c)  # 5

# --- 5. AUGMENTED ASSIGNMENT ---
# Instead of writing a = a + 3, we can write a += 3

x = 10
x += 3    # x = 13
x -= 2    # x = 11
x *= 4    # x = 44
x /= 2    # x = 22.0
x %= 5    # x = 2.0

# --- 6. MODULUS OPERATOR (%) ---
# % returns the remainder of division.
remainder = 10 % 3   # 10 / 3 = 3 remainder 1

# Common use:
# number % 2 == 0 -> even number
# number % 2 != 0 -> odd number

# --- 7. COMPARISON OPERATORS ---
# They compare two values and return True or False.
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

print(1 == 2)  # False
print(1 == 1)  # True
print(1 != 2)  # True
print(1 > 2)   # False
print(1 < 2)   # True
print(1 >= 2)  # False
print(1 <= 2)  # True

# --- 8. LOGICAL OPERATORS ---
# and -> True if both are True
# or  -> True if at least one is True
# not -> reverses the result

result1 = (13 > 12 and 12 < 13)   # True
result2 = (13 > 12 or 13 < 12)    # True
result3 = not (13 < 12)           # True

# ====================================
# 📅 DAY 3 - 10 September 2026
# ====================================

# --- 9. DE MORGAN'S LAWS ---
# not (A and B) == (not A) or (not B)
# not (A or B)  == (not A) and (not B)

# Example 1:
number = 15
result = not (number >= 1 and number <= 10)
# This is the same as: number < 1 or number > 10
print(result)  # True

# Example 2:
is_student = False
is_employed = False
result2 = not (is_student or is_employed)
print(result2)  # True

# ====================================
# 📅 DAY 4 - 11 September 2026
# ====================================

# --- 10. IF STATEMENTS ---
# An if statement runs code only when a condition is True.

# Syntax:
# if condition:
#     code here
# elif another_condition:
#     code here
# else:
#     code here

age = 20
if age > 18:
    status = "Adult"
else:
    status = "Child"
print(status)  # Adult

# Example with elif:
score = 75
if score >= 90:
    grade = "A"
elif score >= 50:
    grade = "B"
else:
    grade = "C"
print(grade)  # B

# --- 11. NESTED IF STATEMENTS ---
# You can put if statements inside other if statements.

age = 20
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
# input() gets text from the user.
# It always returns a string.

# Example:
# name = input("Enter your name: ")
# print("Hello " + name)

# --- 13. TYPE CONVERSION ---
# int()  -> integer
# float() -> decimal number
# str() -> string
# bool() -> boolean

# Example:
# age = int(input("Enter your age: "))
# price = float(input("Enter price: "))

# --- 14. IMPORTANT TIP ---
# "5" + "5" = "55"  # string concatenation
# 5 + 5 = 10        # numeric addition

# So if you want to add numbers from user input, convert them first.

# ====================================
# 📅 DAY 6 - 13 September 2026
# ====================================

# --- 15. WHILE LOOP ---
# A while loop runs while a condition is True.

# Syntax:
# while condition:
#     code

# Example:
count = 1
while count <= 5:
    print(count)
    count += 1

# --- 16. FOR LOOP ---
# A for loop is used to repeat code over a sequence.

# Example:
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# ====================================
# 📅 DAY 7 - 14 September 2026
# ====================================

# --- 17. BREAK AND CONTINUE ---
# continue -> skip the current iteration
# break -> stop the loop completely

# Continue example:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# Break example:
for i in range(10):
    if i == 6:
        break
    print(i)  # 0, 1, 2, 3, 4, 5

# ====================================
# 📅 DAY 8 - 15 September 2026
# ====================================

# --- 18. RANGE() ---
# range(stop) -> starts at 0 and goes up to stop - 1
# range(start, stop) -> starts at start and goes to stop - 1
# range(start, stop, step) -> use custom step size

for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

# ====================================
# 📅 DAY 9 - 16 September 2026
# ====================================

# --- 19. NESTED LOOPS ---
# A nested loop is a loop inside another loop.

for x in range(2):
    for y in range(2):
        print(x, y)

# Output:
# 0 0
# 0 1
# 1 0
# 1 1

# How it works:
# The outer loop runs first.
# For each outer loop value, the inner loop runs completely.
# So the inner loop is repeated many times.

# ====================================
# 📅 DAY 10 - 17 September 2026
# ====================================

# --- 20. FUNCTIONS (def) ---
# A function is a reusable block of code.
# It helps us organize code and avoid repetition.

# Syntax:
# def function_name(parameters):
#     code to run
#     return result (optional)

# Example 1: simple function

def greet(name):
    print(f"Hello {name}")

# Call the function
greet("Pablo")

# Example 2: function that returns a value

def add(a, b):
    return a + b

result = add(5, 7)
print(result)  # 12

# Example 3: function with no parameters

def say_hello():
    print("Hello world")

say_hello()

# Important points:
# - def starts a function definition
# - function_name should be descriptive
# - parameters are values passed into the function
# - return sends a value back to the caller
# - A function is called by writing its name followed by parentheses

# Real-life analogy:
# A function is like a machine.
# Input -> process -> output

# Example:
# def multiply(num1, num2):
#     return num1 * num2
# print(multiply(3, 4))  # 12

# ====================================
# 📅 DAY 11 - 18 September 2026
# ====================================

# --- 21. RETURN STATEMENT ---
# The return statement sends a value back to the caller.
# It is used to get output from a function.

# Syntax:
# def function_name():
#     return value

# Example:
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)  # 5

# Another example:
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# print() vs return
# print() = shows text on the screen, but you cannot use it later
# return = gives the value back so you can store it in a variable

# Example:
def with_print():
    print(10)

# This does not return a useful value:
def with_return():
    return 10

x = with_print()   # x = None
y = with_return()  # y = 10
print(x)
print(y)

# Tip:
# Return ends the function immediately.
# If no return is used, the function returns None by default.

# ====================================
# 📅 DAY 12 - 19 September 2026
# ====================================

# --- 22. DEFAULT PARAMETERS ---
# A default parameter is used when no argument is supplied.

# Correct:
def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_with_default("Pablo"))                  # Hello, Pablo!
print(greet_with_default("Pablo", "Good morning")) # Good morning, Pablo!

# name is a required parameter.
# greeting is a default parameter.

# Incorrect:
# def greet(greeting="Hello", name):
#     return f"{greeting}, {name}!"

# This causes a SyntaxError because a required parameter
# cannot come after a default parameter.

# Rule:
# Required parameters must come first.
# Default parameters come after them.

# Another example:
def introduce(name, age=18):
    return f"My name is {name} and I am {age} years old."

print(introduce("Pablo"))      # Uses the default age: 18
print(introduce("Pablo", 20))  # Uses the provided age: 20

# Summary:
# - A default parameter already has a value.
# - You can replace the default by passing another argument.
# - Required parameters must be written before default parameters.

# ====================================
# 📅 DAY 13 - 20 September 2026
# ====================================

# --- 23. LIST BASICS ---
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

# --- 24. ACCESSING LIST ITEMS ---
# Indexing starts at 0, not 1.

letters = ["a", "b", "c", "d", "e"]
print(letters[0])   # a: first item
print(letters[2])   # c: third item
print(letters[-1])  # e: last item

# The last item can also be accessed with:
# letters[len(letters) - 1]

# --- 25. MODIFYING LIST ITEMS ---
# Use an index to replace an item.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

# --- 26. LOOPING THROUGH A LIST ---
# Loop directly through the values when you do not need indexes.

for fruit in fruits:
    print(fruit)

# Use range(len(list)) when you need the index.
for index in range(len(fruits)):
    print(index, fruits[index])

# enumerate() is a cleaner way to get both the index and value.
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- 27. LIST LENGTH ---
# len() returns the number of items in a list.
print(len(fruits))  # 3

# ====================================
# 📅 DAY 15 - 22 September 2026
# ====================================

# --- 28. BASIC LIST METHODS ---
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
# 📅 DAY 16 - 23 September 2026
# ====================================

# --- 29. TUPLES ---
# A tuple is an immutable (read-only) data structure.
# It is created using parentheses ().
# You access elements using indexing, including negative indexing.

coordinates = (67, 678)

# Accessing elements
x = coordinates[0]  # 67
y = coordinates[1]  # 678

# LIST vs TUPLE
my_list = [1, 2, 3]     # Mutable (can change)
my_tuple = (1, 2, 3)    # Immutable (cannot change)

my_list[0] = 10  # This works
# my_tuple[0] = 10  # This does not work

# TIP:
# Use a list when you need to change it.
# Use a tuple when you want it to stay fixed.

# ====================================
# 📅 DAY 17 - 24 September 2026
# ====================================

# --- 30. ENUMERATE() ---
# enumerate() allows looping through a sequence
# while keeping track of the index of each item.

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Output:
# Index 0: apple
# Index 1: banana
# Index 2: orange

# --- 31. STRING METHODS ---
# String methods can be used to perform actions on strings.

# lower(): converts a string to lowercase
text = "HELLO"
print(text.lower())  # hello

# --- 32. ITERATING OVER STRINGS ---
# A string is a sequence of characters.
# You can loop through a string one character at a time.

text = "Hello"

for character in text:
    print(character)

# You can also iterate through a string using its index.
for index in range(len(text)):
    print(text[index])

# ====================================
# DAY 18 - 25 September 2026
# ====================================

# --- 33.JOINING A LIST INTO A STRING---
# join() combines the items in a list into one string 
# The string before .join() is used as separator

words = ["Hello", "World","Python"]

text = " " .join(words) # Joins with a space
print(text) # Hello World Python 

fruit = ["apple", "banana", "cherry"]
line = ",".join(fruits) # Join with a comma 
print(line) # apple,banana,cherry 

# ---34. LIST SLICING---
# Slicing extracts a portion of a list 
# The start index is included,but the stop is excluded

numbers = [0, 1, 2,3, 4, 5, 6, 7, 8, 9]

# Basic slicing 
print(numbers[2:6]) # [2, 3, 4, 5]

# Omitting start begins from index 0
print(numbers[:5]) # [0, 1, 2, 3, 4,]

# Omitting stop goes until the end 
print(numbers[5:]) # [5, 6, 7, 8, 9]

# Syntax;
# list[start:stop]
# start is inclusive,stop is exclusive
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
