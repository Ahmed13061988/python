todos = []

while True:
    users_input = input("Type add, show, edit, completed exit: ").strip().lower()
    match users_input:
        case "add":
            todo = input("Enter the todo: ")
            todos.append(todo.capitalize())
        case "show" | "display":
            for index, i in enumerate(todos):
                print(f"{index + 1}-{i}")
        case "edit":
            number = int(input("Number of todo to edit?: ")) - 1
            editable = todos[number]
            new_value = input("Edit it: ")
            todos[number] = new_value.capitalize()
        case "completed":
            item = input("What number is done?: ").capitalize()
            todos.remove(item)
            print(f"You're done with {item}")
        case "exit":
            print("Bye!")
            break
        case _:
            print("Please enter a valid command!")






