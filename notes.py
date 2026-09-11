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

# --- 8. LOGICAL OPERATORS
# They combine comparison results and returns True or False 

# and -> Returns True if both conditions are True 
# Example:(13 > 12 and 12 < 13) returns True 
# Example:(13 > 12 and 13 < 12) returns False

# or -> Returns True if at least one is True 
# Example:(13 > 12 or 13 < 12) returns True 
# Example:(13 < 12 or 13 == 12) returns False

# not -> Flips the result,True becomes False and False becomes True 
# Example: not(13 > 12)returns False 
# Example: not(13 < 12) returns True 

# Example 1: 
var1 = 13 
var2 = 12 
result = var1 > var2 and var2 < var1 #result will be True 

# Example 2: 
var1 = 13 
var2 = 12 
result = var1 > var2 or var2 < var1 #result wwil be True 

# Example 3: 
var1 = 13 
var2 = 12 
result = not var1 < var2 #results will be True 

# ====================================
# 📅 DAY 3 - 10 September 2026
# ====================================

# --- 9. DE MORGAN'S LAWS ---
# Rules for how to distribute 'not' over 'and' / 'or'.
# Very useful for simplifying conditions

# Rule 1:not (A and B) becomes (not A) or (not B)
# Rule 2:not (A or B) becomes (not A) and (not B) 

# 💡 Tip:The FLIP Rule 
# When you distribute 'not' 
# 1. Each part gets 'not'
# 2. The operator FLIPS; and <-> or 

# Examples:
# First Law example:
number = 15 
result = not(number >= 1 and number <=10)
# This becomes: (not number >= 1) or (not number <= 10) 
# Simplimfied: number < 1 or number > 10
print(result) # True,because 15 > 10 

# Second Law example:
is_student = False
is_employed = False 
result2 = not(is_student or is_employed)
# This becomes: (not is_student) and (not is_employed)
print(result2) #True

# ====================================
# 📅Day 4 - 11 September 2026
# ====================================

# ---10. IF STATEMENTS ---
# if statements allow conditional execution of code.
# The codes runs only if the condition is True.

# Sytanx:
# if conditiosn:
# Indented code block.
# Executed if condition is True.

# Tip: Rule for if/elif/else 
# 1.Code inside if,elif,and else block MUST be indented.
# 2.Use a colon (:) after the condition.
# 3.Indent the code block with 4 spaces or a tab.
# 4.You can have multiple elif statements.
# 5.The else block is optional and execute when no conditions are met.

# Examples:
age = 20 
status = "child"
if age > 18:
  status = "Adult"
age += 1 
print(status) #Adult,because 20 > 18 

# Example with elif and else 
score = 75 
if score >= 90:
  print("A")
elif score >= 50:
  print("B") # Thia will print
else:
  print("C")

# Example 2 
if condition:
  code
elif another_condition:
  code
else:
  code

# ---11. NESTED IF-ELIF-ELSE---
# Nested statement allow for hierarchical decision making. 
# You put an if inside another if.

# Sytanx:
# if condition1: 
#   if conditions2:
#     # Code when both condition1 and condition2 are True
#   else:
#     # Code when condition1 is true but condition2 is false
# else:
#  # Code when condition1 is false

# Example of nested conditions
age = 20 
has_license = True

if age > 18:
  if has_lincese:
    print("You can drive")
  else:
    print("Get a lincense first")
else:
  print("Too young to drive")

# 💡Tip:Nesting can be infinite,but don't overdo it.
# You can do if inside if inside if.....

# if condition1:
#    if condition2:
#       if condition3:
#          # More nested condition....
#          print("All conditions true")

# Simple rule: The more indented,the deeper the check
