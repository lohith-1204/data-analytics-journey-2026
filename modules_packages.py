# Modules, Packages, Libraries & Import

# Importing Built-in Module

import math

print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

# Import Specific Functions

from math import sqrt, pow

print("\nUsing direct import:")
print("sqrt(25):", sqrt(25))
print("2^3:", pow(2, 3))

# Import with Alias

import math as m

print("\nUsing alias:")
print("sqrt(36):", m.sqrt(36))

# Custom Module

# Assume we have a file: mymodule.py
# with a function: greet()

# from mymodule import greet
# greet()

# Random Library Example

import random

print("\nRandom number:", random.randint(1, 10))