print("\n===== Menu =====")
print("1. Add")
print("2. Subtract")
print("3. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Addition selected")
    case 2:
        print("Subtraction selected")
    case 3:
        print("Exiting...")
    case _:
        print("Invalid option")