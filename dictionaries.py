# Dictionaries in Python

# Creating a Dictionary

student = {
    "name": "Lohith",
    "age": 21,
    "course": "ISE"
}

print("Original Dictionary:", student)

# Accessing Values

print("\nName:", student["name"])
print("Age:", student.get("age"))

# Adding / Updating Elements

# Add new key-value pair
student["grade"] = "A"
print("\nAfter adding grade:", student)

# Update value
student["age"] = 22
print("After updating age:", student)

# 4. Removing Elements

# Remove specific key
student.pop("course")
print("\nAfter pop:", student)

# Remove last inserted item
student.popitem()
print("After popitem:", student)

# Dictionary Methods

student = {
    "name": "Lohith",
    "age": 21,
    "course": "ISE"
}

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Looping Through Dictionary

print("\nLoop through keys:")
for key in student:
    print(key)

print("\nLoop through values:")
for value in student.values():
    print(value)

print("\nLoop through key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Built-in Functions

print("\nLength of dictionary:", len(student))

# Copy dictionary
copy_dict = student.copy()
print("Copied dictionary:", copy_dict)