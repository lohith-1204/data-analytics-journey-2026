#Creating Strings
str1 = "Hello"
str2 = 'Python'
str3 = """This is a multi-line string"""

print("String 1:", str1)
print("String 2:", str2)
print("String 3:", str3)

full = str1 + " " + str2 # Concatenation
print("\nConcatenation:", full)

print("Repetition:", str1 * 3) # Repetition

print("\nFirst character:", str1[0]) #Indexing
print("Last character:", str1[-1])

# Slicing
print("\nSlicing (0:3):", str1[0:3])
print("Slicing (1:):", str1[1:])
print("Slicing (:4):", str1[:4])

text = "hello world" # String Methods

print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Replace:", text.replace("world", "Python"))

print("\nLength of string:", len(text)) # String length