# Python Notes - Day 12
# Date: 19 September 2026
# Topic: Default Parameters and Parameter Order

# Required parameters must come before parameters with default values.

# Correct:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Pablo"))                 # Hello, Pablo!
print(greet("Pablo", "Good morning")) # Good morning, Pablo!

# name is a required parameter.
# greeting is a default parameter because it already has a value.

# Incorrect:
# def greet(greeting="Hello", name):
#     return f"{greeting}, {name}!"

# This causes a SyntaxError because a required parameter (name)
# cannot come after a default parameter (greeting).

# Rule:
# Required parameters come first.
# Default parameters come after required parameters.

# Correct order:
# def function(required_parameter, default_parameter="default value"):
#     code

# Another example:
def introduce(name, age=18):
    return f"My name is {name} and I am {age} years old."

print(introduce("Pablo"))       # Uses the default age: 18
print(introduce("Pablo", 20))   # Uses the provided age: 20

# Summary:
# - A default parameter already has a value.
# - You can replace the default by passing another argument.
# - Required parameters must be written before default parameters.
