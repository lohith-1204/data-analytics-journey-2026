# String Access and Manipulation

text = "Hello Python"

print("Original String:", text)

# Accessing Characters (Indexing)

print("\nFirst character:", text[0])
print("Last character:", text[-1])

# Slicing

print("\nFirst 5 characters:", text[:5])
print("From index 6 to end:", text[6:])
print("Middle part:", text[3:9])

# String Manipulation Methods

# Uppercase
print("\nUppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Replace
print("Replace:", text.replace("Python", "World"))

# Split
words = text.split()
print("Split into words:", words)

# Join
joined = "-".join(words)
print("Joined string:", joined)

# Checking Strings

print("\nStarts with 'Hello':", text.startswith("Hello"))
print("Ends with 'Python':", text.endswith("Python"))
print("Is alphabetic:", text.isalpha())


# Removing Spaces


extra = "   Hello   "
print("\nBefore strip:", extra)
print("After strip:", extra.strip())