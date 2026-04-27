# File Handling in Python

# Write to a File (Create/Overwrite)

file = open("sample.txt", "w")
file.write("Hello, this is a file.\n")
file.write("Learning Python file handling.")
file.close()

print("File written successfully.")

# Read from a File

file = open("sample.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()

# Append to a File

file = open("sample.txt", "a")
file.write("\nThis line is appended.")
file.close()

print("\nData appended successfully.")

# Using 'with' (Best Practice)

with open("sample.txt", "r") as file:
    print("\nReading using with:")
    print(file.read())

# Read Line by Line

with open("sample.txt", "r") as file:
    print("\nLine by line:")
    for line in file:
        print(line.strip())