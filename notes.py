# Python Notes - My Learning Journey
# Started: 08 September 2026

# Table of Contents
# - DAY 1 (08 Sep 2026)
#   1. Variables
#   2. Strings
#   3. Booleans
# - DAY 2 (09 Sep 2026)
#   4. Arithmetic operators (+ - * / // % **)
#   5. Augmented assignment (+=, -=, ...)
#   6. Modulus operator (%)
#   7. Comparison operators (==, !=, >, <, >=, <=)
#   8. Logical operators (and, or, not)
# - DAY 3 (10 Sep 2026)
#   9. De Morgan's laws
# - DAY 4 (11 Sep 2026)
#   10. If / elif / else
#   11. Nested ifs
# - DAY 5 (12 Sep 2026)
#   12. input(), Casting, String vs numeric addition
# - DAY 6 (13 Sep 2026)
#   16. Loops: while, for
# - DAY 7 (14 Sep 2026)
#   18. break and continue
# - DAY 8 (15 Sep 2026)
#   19. range() usage and examples
# - DAY 9 (16 Sep 2026)
#   20. Nested loops
# - Examples runner
#   Safe demo examples that run only when executing the file directly

# ====================================
# 📅 DAY 1 - 08 September 2026
# ====================================

# 1. VARIABLES
# A variable is a container that holds data values.
# It is used to store, manipulate, and display information.
# Python automatically detects the data type.

# Examples:
# variable_name = value
age = 20
score = 2100

# Tip: Spaces in Python
# Variable names CANNOT use spaces. Use underscore (_) instead (snake_case).
# Examples:
# my score = 100  ❌ Wrong
# my_score = 10000 ✅ Correct

# 2. STRINGS (str)
# A string stores text in Python.
text1 = 'This is a sentence'
text2 = "This is also a sentence"

# Tip:
# To create a string, use single ('') or double ("") quotes around the text.

# 3. BOOLEANS (bool)
# A boolean is a data type with only two values: True or False.
variable_true = True
variable_false = False

# Tip: Case sensitive
# true  ❌ Wrong
# True  ✅ Correct

# ====================================
# 📅 DAY 2 - 09 September 2026
# ====================================

# 4. ARITHMETIC OPERATORS
# +  addition
# -  subtraction
# *  multiplication
# /  division (float division in Python 3)
# // integer (floor) division
# %  modulus (remainder)
# ** exponentiation

# Example:
a = 2
b = 3
c = a + b  # c == 5

# 5. AUGMENTED ASSIGNMENT (in-place) OPERATORS
# Instead of writing a = a + 3 you can write a += 3

# Example sequence (independent examples):
a = 10
# a += 3  -> a becomes 13
# a -= 3  -> a becomes 7
# a *= 3  -> a becomes 30
# a /= 3  -> a becomes 3.333...
# a %= 3  -> a becomes 1

# 6. MODULUS OPERATOR (%) - gives remainder of a division
# Example:
# results = 10 % 3  # 10 / 3 => remainder 1, so results == 1

# Common use: check if number is even or odd
# Even: number % 2 == 0
# Odd:  number % 2 == 1

# 7. COMPARISON OPERATORS
# They compare two values and return True or False (Boolean).
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to

# Examples (read-only; these show expected boolean results):
_example_eq = (1 == 2)   # False
_example_eq2 = (1 == 1)  # True
_example_ne = (1 != 2)   # True
_example_gt = (1 > 2)    # False
_example_lt = (1 < 2)    # True
_example_ge = (1 >= 2)   # False
_example_le = (1 <= 2)   # True

# 8. LOGICAL OPERATORS
# and -> True if both operands are True
# or  -> True if at least one operand is True
# not -> negates the boolean value

# Example (conceptual):
# (a > b) and (b < c)
# (a > b) or (b < c)
# not (a > b)

# ====================================
# 📅 DAY 3 - 10 September 2026
# ====================================

# 9. DE MORGAN'S LAWS
# not (A and B) == (not A) or (not B)
# not (A or B)  == (not A) and (not B)
# When you distribute not, flip and <-> or

# Example (conceptual):
# not (x > 0 and x < 10)  <==>  (x <= 0) or (x >= 10)

# ====================================
# 📅 DAY 4 - 11 September 2026
# ====================================

# 10. IF STATEMENTS
# Conditional execution:
# if condition:
#     indented code runs only if condition is True

# Tips for if / elif / else:
# - Use a colon (:) after the condition
# - Indent the block (4 spaces recommended)
# - You can have multiple elifs; else is optional

# Example:
# age = 20
# if age > 18:
#     status = 'adult'
# else:
#     status = 'child'

# Example with elif / else:
# score = 75
# if score >= 90:
#     grade = 'A'
# elif score >= 50:
#     grade = 'B'
# else:
#     grade = 'C'

# 11. NESTED IF / ELIF / ELSE
# You can put an if inside another if for hierarchical decisions.
# Keep nesting depth reasonable for readability.

# Example:
# age = 20
# has_license = True
# if age > 18:
#     if has_license:
#         print('You can drive')
#     else:
#         print('Get a license first')
# else:
#     print('Too young to drive')

# ====================================
# 📅 DAY 5 - 12 September 2026
# ====================================

# 12. input() FUNCTION
# Use input() to get text from a user.
# Always returns a string.

# Example (do not call during automated runs):
# name = input('Enter your name: ')
# print('Hello, ' + name)

# 13. CASTING (CONVERSION)
# Convert between types when needed.
# int()   -> integer (whole number)
# float() -> floating point (decimal)
# str()   -> string
# bool()  -> boolean (Note: bool(non-empty-string) is True)

# Examples:
# age = int(input('Enter your age: '))   # "20" -> 20
# price = float(input('Enter price: '))  # "9.99" -> 9.99

# 14. IMPORTANT DIFFERENCE
# Adding strings concatenates them, while adding numbers performs arithmetic
# "5" + "5" == "55"  # string concatenation
# 5 + 5 == 10            # numeric addition

# So you MUST cast when reading numbers from input:
# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)  # outputs 10 if user enters 5 and 5

# 15. MULTIPLE INPUTS
# Ask for input multiple times if you need multiple values.
# Example:
# first_name = input('First name: ')
# last_name = input('Last name: ')
# print(first_name + ' ' + last_name)

# ====================================
# 📅 DAY 6 - 13 September 2026
# ====================================

# 16. LOOPS: WHILE
# A while loop runs as long as a condition is True.
# Use a while loop when you don't know beforehand how many times it will run.

# Syntax:
# while condition:
#     code

# Example:
# number = 27
# power_of_two = 1
# while power_of_two <= number:
#     power_of_two *= 2  # update to avoid infinite loop
# # After the loop, power_of_two is 32

# Important points:
# - Ensure you update the variable used in the condition (or use a break) to avoid infinite loops
# - You can use while True: with a break to create a loop that stops on a condition

# 17. LOOPS: FOR
# A for loop is used to iterate over a sequence (like a list or range)

# Syntax:
# for i in range(start, stop[, step]):
#     code

# Range examples:
# - range(stop): starts from 0, goes up to (but not including) stop
# - range(start, stop): goes from start to (but not including) stop
# - range(start, stop, step): steps by step (step can be negative)

# Examples:
# for i in range(5):
#     print(i)  # 0,1,2,3,4

# for i in range(1, 6):
#     print(i)  # 1,2,3,4,5

# Tip:
# - Use while when you don't know how many iterations are needed
# - Use for + range() when you know (or can compute) how many iterations

# ====================================
# 📅 DAY 7 - 14 September 2026
# ====================================

# 18. BREAK and CONTINUE
# continue -> skip the current iteration and continue with the next one
# break    -> stop the loop completely

# Examples (commented so file is import-safe):
# for i in range(3, 9):
#     if i == 5:
#         continue  # skip 5
#     print(i)     # 3, 4, 6, 7, 8

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i, "is odd")

# for i in range(10):
#     if i == 6:
#         break
#     print(i)     # 0, 1, 2, 3, 4, 5

# Example - stop when you find first number divisible by 7
# for i in range(1, 100):
#     if i % 7 == 0:
#         print(f"Found it: {i}")
#         break

# SUMMARY:
# continue -> skip this one, keep looping
# break    -> stop the loop

# ====================================
# 📅 DAY 8 - 15 September 2026
# ====================================

# 19. range() - 3 ways to use it
# 1. range(stop): starts from 0, goes up to stop (stop is NOT included), step == 1
# 2. range(start, stop): starts at start (inclusive), goes up to stop (exclusive), step == 1
# 3. range(start, stop, step): starts at start, goes up to stop (exclusive), steps by step

# Important notes:
# - start is inclusive, stop is exclusive (stop value is not included)
# - step can be positive (count up) or negative (count down)
# - to go backwards, step must be negative (e.g. -1, -2)

# Examples (commented so file is import-safe):
# # Counts from 0 to 4
# for i in range(5):
#     print(i)

# # Counts from 2 to 5
# for i in range(2, 6):
#     print(i)

# # Counts odd numbers from 1 to 9
# for i in range(1, 10, 2):
#     print(i)

# # Counts down by 2s from 10 down to 2
# for i in range(10, 0, -2):
#     print(i)

# Tip:
# - start is inclusive, stop is exclusive
# - step can be positive or negative
# - to go backwards, step must be negative (e.g. -1, -2)

# ====================================
# 📅 DAY 9 - 16 September 2026
# ====================================

# 20. NESTED LOOPS
# Nested loops are loops inside other loops.

# Syntax example:
# for x in range(2):
#     for y in range(2):
#         print(x, y)
#
# Output:
# 0 0
# 0 1
# 1 0
# 1 1

# How it works:
# - The inner loop completes all iterations for each iteration of the outer loop
# - Similar to how a clock's minute hand completes a full cycle for each hour
# - Outer loop = hour, Inner loop = minute

# Example breakdown:
# for x in range(2):      # x = 0 first
#     for y in range(2):  # y = 0, then 1
#         print(x, y)     # prints 0 0, then 0 1
#
#     # then x = 1
#     # y = 0, then 1 again
#     # prints 1 0, then 1 1

# Tip:
# - Outer loop runs slower, inner loop runs faster ✅
# - If outer is range(3) and inner is range(2), total prints = 3 * 2 = 6 times

# ====================================
# Examples runner (safe): only runs when executed directly
# ====================================

# ====================================
# DAY 10 - 17 September 2026
# ====================================

# 21. FUNCTIONS IN PYTH0N 
# A function is a block of code that runs only when you call it
# Used to avoid repeating same code

# Sytanx example:
# Function declaration
def funtion_name():
    #function body(indented)
    code_here

# Function call
function_name()

# Function Arguments 
# Arguments are values passed into a function when calling it

def function_name(arg1,arg2,...)
    # function code
function _name (value1,value2,....)
 # Examples 
def greet(name):
    print(f"Hello{name}")

greet("Pablo") # Hello Pablo

def add(a,b):
    print(a+b)

add (2,3) # 5

# Important 
# -Number of arguments must match number of values 
# -Passing wrong number will cause program to fail 
# -def = defining,call using 

# Tip 
# Think of function like a machine: arg = input you put in,call =pressing the start button 
def _demo():
    # Small runnable examples to try when you run `python notes.py`
    print('Arithmetic: 2 + 3 =', 2 + 3)
    print('Modulus: 10 % 3 =', 10 % 3)
    print('Comparison: 1 == 2 ->', 1 == 2)

    # While loop example:
    number = 27
    power_of_two = 1
    while power_of_two <= number:
        power_of_two *= 2
    print('Small while example result (power_of_two):', power_of_two)

    # Range examples:
    print('range(5):', list(range(5)))
    print('range(2,6):', list(range(2, 6)))
    print('range(1,10,2):', list(range(1, 10, 2)))
    print('range(10,0,-2):', list(range(10, 0, -2)))

    # Nested loops example (demonstration):
    pairs = [(x, y) for x in range(2) for y in range(2)]
    print('Nested loop pairs (range(2), range(2)):', pairs)


if __name__ == '__main__':
    _demo()
