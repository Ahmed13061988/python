todos = []

while True:
    users_input = input("Type add, show, edit or exit: ").strip().lower()
    match users_input:
        case "add":
            todo = input("Enter the todo: ")
            todos.append(todo.capitalize())
        case "show" | "display":
            for i in todos:
                print(i)
        case "edit":
            number = int(input("Number of todo to edit?: ")) - 1
            editable = todos[number]
            new_value = input("Edit it: ")
            todos[number] = new_value.capitalize()
        case "exit":
            print("Bye!")
            break
        case _:
            print("Please enter a valid command!")






