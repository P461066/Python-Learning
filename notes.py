# Python Notes - My Learning Journey
# Started: 08 September 2026

# ====================================
# 📅 DAY 1 - 08 September 2026
# ====================================

# --- 1. VARIABLES ---
# A variable is like a container that holds data values.
# It is used to store, manipulate, and display information.
# Python automatically detects the data type.

# Examples:
# variable_name = value
age = 20
score = 2100

# 💡 Tip: Spaces in Python
# Variable names CANNOT use spaces. We use underscore (_) instead.
# This style is called snake_case.

# Examples:
# my score = 100  ❌ Wrong spaces not allowed
# my_score = 10000  ✅ Correct

# --- 2. STRING (str) ---
# A string is used to create/store text or a sentence in Python.

# Examples:
text1 = 'This is a sentence'
text2 = "This is also a sentence"

# 💡 Tip: 
# To create a string you have to use single (' ') or double (" ") quotes around the text.

# --- 3. BOOLEAN (bool) ---
# A boolean is a data type that has only 2 possible values: True or False.
# It is used to check whether a condition is true or false.

# Examples:
variable_true = True
variable_false = False

# 💡 Tip: Case Sensitive!
# Boolean must start with a capital T or F.
# true  ❌ Wrong
# True  ✅ Correct

# ====================================
# 📅 DAY 2 - 09 September 2026
# ====================================

# --- 4. ARITHMETIC OPERATORS ---

# 1. Addition (+)
# Example: 3 + 2 = 5

# 2. Subtraction (-)
# Example: 3 - 2 = 1

# 3. Multiplication (*)
# Example: 3 * 2 = 6

# 4. Division (/)
# Example: 4 / 2 = 2

# Example Usage:
a = 2
b = 3
c = a + b  # c will be 5
print(c)

# --- 5. SHORTCUT OPERATORS (Self arithmetic)
# instead of writing a = a + 3,we can write a += 3 (faster way)

# Addition shortcut (+=)
a = 10 
a += 3 # same as a = a + 3 -> is now 13 

# Subtraction shortcut (-=)
a -= 3 # same as a = a - 3 -> 7 

# Multiplication shortcut (*=)
a *= 3 # same as a = a * 3 -> is now 30 

# Division shortcut (/=)
a /= 3 # same as a = a / 3 -> is now 3.33

# Modulus shortcut (%=) 
a %= 3 # same as a = a % 3 -> is now 1

# --- 6. MODULUS OPERATOR (%) - VERY IMPORTANT 
# % gives you the REMAINDER of a division 

results = 10 % 3 # 10 /  3 = 3 remainder 1, so results is 1 

# Common use: Check if number is even or odd 
# Even: number % 2 == 0 
# Odd: number % 2 == 1 

# --- 7. COMPARISON OPERATORS 
# Comparison operators compare 3 values and return True or False (Boolean)

# == Equal to 
print(1 == 2) # False, because 1 is not equal to 2
print(1 == 1) # True 

# != Not equal to 
print(1 != 2) # True,because 1 is not equal to 2 

# > Greater than 
print(1 > 2) # False,because 1 is not greater than 2 

# < Less than 
print(1 < 2) # True,1 is less than 2 

# >= Greater than or equal to 
print(1 >= 2) # False 

# <= Less than or equal to 
print(1 <= 2) # True 

# Example 1: 
var1 = 13 
var2 = 12 
var3 = var1 != var2 # var3 will be True because 13 is not equal to 12
print(var3)

# Example 2:
var1 = 13 
var2 = 13
var3 = var1 == var2 #var2 will be True because both are 13 
print(var3)
