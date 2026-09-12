# Python Notes - My Learning Journey
# Started: 08 September 2026

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
# /  division (float division)

# Example:
a = 2
b = 3
c = a + b  # c == 5

# 5. SHORTCUT (IN-PLACE) OPERATORS
# Instead of writing a = a + 3 you can write a += 3

# Example sequence (shown as independent examples):
a = 10
a += 3  # a == 13

a = 10
a -= 3  # a == 7

a = 10
a *= 3  # a == 30

a = 10
a /= 3  # a == 3.333...

a = 10
a %= 3  # a == 1

# 6. MODULUS OPERATOR (%) - gives remainder of a division
results = 10 % 3  # 10 / 3 => remainder 1, so results == 1

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

# Examples:
_example_eq = (1 == 2)  # False
_example_eq2 = (1 == 1)  # True
_example_ne = (1 != 2)  # True
_example_gt = (1 > 2)   # False
_example_lt = (1 < 2)   # True
_example_ge = (1 >= 2)  # False
_example_le = (1 <= 2)  # True

var1 = 13
var2 = 12
var3 = var1 != var2  # True

var1 = 13
var2 = 13
var3 = var1 == var2  # True

# 8. LOGICAL OPERATORS
# and -> True if both operands are True
# or  -> True if at least one operand is True
# not -> negates the boolean value

# Examples:
var1 = 13
var2 = 12
result_and = (var1 > var2 and var2 < var1)  # True
result_or = (var1 > var2 or var2 < var1)   # True
result_not = (not (var1 < var2))           # True

# ====================================
# 📅 DAY 3 - 10 September 2026
# ====================================

# 9. DE MORGAN'S LAWS
# not (A and B) == (not A) or (not B)
# not (A or B)  == (not A) and (not B)
# When you distribute not, flip and <-> or

# Examples:
number = 15
result = not (number >= 1 and number <= 10)
# Equivalent: number < 1 or number > 10

is_student = False
is_employed = False
result2 = not (is_student or is_employed)
# Equivalent: (not is_student) and (not is_employed)

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
age = 20
status = "child"
if age > 18:
    status = "adult"
# age += 1  # changing age after the check won't change the result above

# Example with elif / else:
score = 75
if score >= 90:
    grade = "A"
elif score >= 50:
    grade = "B"
else:
    grade = "C"

# 11. NESTED IF / ELIF / ELSE
# You can put an if inside another if for hierarchical decisions.
# Keep nesting depth reasonable for readability.

age = 20
has_license = True

if age > 18:
    if has_license:
        drive_message = "You can drive"
    else:
        drive_message = "Get a license first"
else:
    drive_message = "Too young to drive"

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

# Demo runner: put examples that print under this guard so importing this file won't execute them.

def _demo():
    print('Arithmetic example: 2 + 3 =', 2 + 3)
    print('Modulus example: 10 % 3 =', 10 % 3)
    print('Comparison example: 1 == 2 ->', 1 == 2)
    print('De Morgan example (15):', result)
    print('Drive message:', drive_message)
    print('Grade for score 75:', grade)


if __name__ == '__main__':
    _demo()
