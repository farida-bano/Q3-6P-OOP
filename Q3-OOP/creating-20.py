# 20. Creating a Custom Exception
# Assignmemt
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return "Age is valid"

# Test the function
try:
    age = 16  # You can change this value to test different cases
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")
