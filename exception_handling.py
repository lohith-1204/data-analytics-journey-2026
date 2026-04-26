# Errors and Exception Handling

# Basic Exception Handling

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input!")

# Using else

try:
    x = int(input("\nEnter a number: "))
    print("You entered:", x)

except ValueError:
    print("Invalid input!")

else:
    print("No error occurred!")

# Using finally

try:
    print("\nTrying something...")
    num = 10 / 2

except:
    print("Error occurred!")

finally:
    print("This will always execute")

# Multiple Exceptions

try:
    num = int(input("\nEnter number: "))
    print(100 / num)

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# Custom Exception

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("\nEnter positive number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed!")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Error:", e)