# Functions, Parameters, Local vs Global Variables

# Defining a Function

def greet():
    print("Hello, welcome to Python!")

greet()

# Function with Parameters

def add(a, b):
    return a + b

result = add(10, 5)
print("\nAddition Result:", result)

# Default Parameters

def greet_user(name="Guest"):
    print("Hello,", name)

greet_user("Lohith")
greet_user()

# Local Variable

def local_example():
    x = 10  # local variable
    print("\nLocal x:", x)

local_example()

# Global Variable

x = 100  # global variable

def global_example():
    print("\nGlobal x inside function:", x)

global_example()

# Modifying Global Variable

count = 0

def update_count():
    global count
    count += 1

update_count()
print("\nUpdated global count:", count)