command = input("Enter command: ")

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")