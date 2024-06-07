while True:
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()
    match users_input:
        case "add":
            todo = input("Enter the todo: ") + "\n"
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            todos.append(todo.capitalize())
            file.close()
            file = open("files/todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            new_todos = [item.strip("\n") for item in todos]
            for index, i in enumerate(new_todos):
                print(f"{index + 1}-{i}")
        case "edit":
            number = int(input("Number of todo to edit?: ")) - 1
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            editable = todos[number]
            new_value = input("Edit it: ")
            todos[number] = new_value.capitalize()
            file = open("files/todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "complete":
            item = int(input("What number is done?: "))
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.pop(item-1)
            print(f"You're done with {item}")
        case "exit":
            print("Bye!")
            break
        case _:
            print("Please enter a valid command!")






