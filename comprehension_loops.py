# Comprehensions, List Input, Loops Revision

# List Comprehension

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Even numbers using comprehension
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)

# List Input from User

# Input numbers separated by space
user_input = input("\nEnter numbers separated by space: ")

numbers = list(map(int, user_input.split()))
print("List:", numbers)

# Loop Revision (For Loop)

print("\nLoop through list:")
for num in numbers:
    print(num)

# Loop with Index (Enumerate)

print("\nUsing enumerate:")
for index, value in enumerate(numbers):
    print("Index:", index, "Value:", value)

# While Loop Revision

print("\nWhile loop:")
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1