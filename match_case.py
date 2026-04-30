# match-case statement

choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You chose One")
    case 2:
        print("You chose Two")
    case 3:
        print("You chose Three")
    case _:
        print("Invalid choice")