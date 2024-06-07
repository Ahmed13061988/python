while True:
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    if "add" in users_input:
        todo = users_input.replace("add ", "")
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo.capitalize())

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif "show" in users_input:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        new_todos = [item.strip("\n") for item in todos]
        for index, i in enumerate(new_todos):
            print(f"{index + 1}-{i}")
    elif "edit" in users_input:
        number = int(input("Number of todo to edit?: "))
        number = number - 1
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        editable = todos[number]
        new_value = input("Edit it: ") + '\n'
        todos[number] = new_value.capitalize()
        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)
    elif "complete" in users_input:
        item = int(input("What number is done?: "))
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todos.pop(item-1)
        print(f"You're done with {item}")
    elif "exit" in users_input:
        print("Bye!")
        break
    else:
        print("Command is not valid")






