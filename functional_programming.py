# Functional Programming - map, filter, reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() → Apply function to all elements

squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter() → Select elements based on condition

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce() → Reduce list to single value

sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_all)