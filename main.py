while True:
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    if users_input.startswith("add"):
        todo = users_input.replace("add ", "")
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo.capitalize() + "\n")
        print(todos)
        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif users_input.startswith("show"):
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        new_todos = [item.strip("\n") for item in todos]
        for index, i in enumerate(new_todos):
            print(f"{index + 1}-{i}")

    elif users_input.startswith("edit"):
        try:
            number = users_input[5:]
            number = int(number) - 1
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_value = input("Edit it: ") + '\n'
            todos[number] = new_value.capitalize()
            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid!")
            continue
    elif users_input.startswith("complete"):
        try:
            item = int(users_input[8:])
            item = item - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(item)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"You're done with {item + 1}")
        except (ValueError, IndexError):
            print("Your command is not valid")
            continue
    elif "exit" in users_input:
        print("Bye!")
        break

    else:
        print("Command is not valid")






