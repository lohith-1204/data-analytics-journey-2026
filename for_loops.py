# For Loops, Range, Enumerate, Nested Loops

# 1. Basic For Loop

print("For Loop Example:")

for i in range(1, 6):
    print(i)

# 2. Range Function

print("\nRange Examples:")

# range(start, stop)
for i in range(2, 6):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

# 3. Loop through List

numbers = [10, 20, 30]

print("\nLoop through list:")
for num in numbers:
    print(num)

# 4. Enumerate

print("\nEnumerate Example:")

for index, value in enumerate(numbers):
    print("Index:", index, "Value:", value)

# 5. Nested Loops

print("\nNested Loop Example:")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)