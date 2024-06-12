def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    if users_input.startswith("add"):
        todo = users_input.replace("add ", "")
        todos = get_todos("files/todos.txt")
        todos.append(todo.capitalize() + "\n")
        write_todos("files/todos.txt", todos)

    elif users_input.startswith("show"):
        todos = get_todos("files/todos.txt")
        new_todos = [item.strip("\n") for item in todos]
        for index, i in enumerate(new_todos):
            print(f"{index + 1}-{i}")

    elif users_input.startswith("edit"):
        try:
            number = users_input[5:]
            number = int(number) - 1
            todos = get_todos("files/todos.txt")
            new_value = input("Edit it: ") + '\n'
            todos[number] = new_value.capitalize()
            write_todos("files/todos.txt", todos)
        except ValueError:
            print("Your command is not valid!")
            continue
    elif users_input.startswith("complete"):
        try:
            item = int(users_input[8:])
            item = item - 1
            todos = get_todos("files/todos.txt")
            todos.pop(item)
            write_todos("files/todos.txt", todos)
            print(f"You're done with {item + 1}")
        except (ValueError, IndexError):
            print("Your command is not valid")
            continue
    elif "exit" in users_input:
        print("Bye!")
        break

    else:
        print("Command is not valid")
