# OOP Pillars - Inheritance & Polymorphism

# Inheritance

# Parent Class
class Animal:
    
    def speak(self):
        print("Animal makes a sound")


# Child Class
class Dog(Animal):
    
    def bark(self):
        print("Dog barks")


# Create object
dog = Dog()

dog.speak()  # inherited method
dog.bark()   # own method


#  Method Overriding (Polymorphism)

class Animal:
    
    def speak(self):
        print("\nAnimal makes a sound")


class Cat(Animal):
    
    def speak(self):   # overriding parent method
        print("Cat meows")


cat = Cat()
cat.speak()


# Operator Polymorphism

print("\nOperator Polymorphism:")

print(5 + 3)        # addition
print("Hello " + "World")  # string concatenation


# Function Polymorphism

print("\nFunction Polymorphism:")

print(len("Python"))   # length of string
print(len([1, 2, 3]))  # length of list