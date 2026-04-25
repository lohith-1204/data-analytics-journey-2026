# SOLID Principles in Python

# Single Responsibility Principle (SRP)

class Report:
    def generate(self):
        print("Generating report...")

class ReportPrinter:
    def print_report(self):
        print("Printing report...")

# Open/Closed Principle (OCP)

class Discount:
    def apply(self, amount):
        return amount

class PercentageDiscount(Discount):
    def apply(self, amount):
        return amount * 0.9

# Liskov Substitution Principle (LSP)

class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

# Interface Segregation Principle (ISP)

class Worker:
    def work(self):
        pass

class Eat:
    def eat(self):
        pass

class Human(Worker, Eat):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")

# Dependency Inversion Principle (DIP)

class Keyboard:
    def type(self):
        print("Typing...")

class Computer:
    def __init__(self, keyboard):
        self.keyboard = keyboard

    def start(self):
        self.keyboard.type()

keyboard = Keyboard()
pc = Computer(keyboard)
pc.start()