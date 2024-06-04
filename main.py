todos = []

while True:
    users_input = input("Type add, show or exit: ").strip().lower()
    match users_input:
        case "add":
            todo = input("Enter the todo: ")
            todos.append(todo.capitalize())
        case "show":
            for i in todos:
                print(i)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Please enter a valid command!")



