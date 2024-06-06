while True:
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()
    match users_input:
        case "add":
            todo = input("Enter the todo: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            todos.append(todo.capitalize())
            file.close()
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open("todos.txt", "r")
            todos = file.readlines()
            for index, i in enumerate(todos):
                print(f"{index + 1}-{i}")
        case "edit":
            number = int(input("Number of todo to edit?: ")) - 1
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            editable = todos[number]
            new_value = input("Edit it: ")
            todos[number] = new_value.capitalize()
        case "complete":
            item = int(input("What number is done?: "))
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.pop(item-1)
            print(f"You're done with {item}")
        case "exit":
            print("Bye!")
            break
        case _:
            print("Please enter a valid command!")






