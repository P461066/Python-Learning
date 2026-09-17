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
# CURRENT TOPIC - Functions / Reusable Code

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
# CURRENT TOPIC: FUNCTIONS / REUSABLE CODE
# ====================================

# When learning functions, remember:
# 1. A function helps organize code
# 2. It makes code reusable
# 3. It can take parameters
# 4. It can return a value
# 5. It makes programs easier to read

# Practice idea:
# Write a function that calculates the area of a rectangle.
# Write a function that checks if a number is even.
# Write a function that adds two numbers.

# Example practice:

def is_even(number):
    return number % 2 == 0

print(is_even(8))  # True
print(is_even(9))  # False

# ====================================
# SAFE DEMO RUNNER
# ====================================

def _demo():
    print("Arithmetic example:", 2 + 3)
    print("Modulus example:", 10 % 3)
    print("Range example:", list(range(1, 10, 2)))

    def greet(name):
        return f"Hello {name}"

    print("Function demo:", greet("Pablo"))


if __name__ == "__main__":
    _demo()
