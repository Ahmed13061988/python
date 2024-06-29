# from functions import get_todos, write_todos
import functions
import time


while True:
    print(time.strftime("%Y:%M"))
    users_input = input("Type add, show, edit, complete or exit: ").strip().lower()

    if users_input.startswith("add"):
        todo = users_input.replace("add ", "")
        todos = functions.get_todos()
        todos.append(todo.capitalize() + "\n")
        functions.write_todos(todos)

    elif users_input.startswith("show"):
        todos = functions.get_todos()
        new_todos = [item.strip("\n") for item in todos]
        for index, i in enumerate(new_todos):
            print(f"{index + 1}-{i}")

    elif users_input.startswith("edit"):
        try:
            number = users_input[5:]
            number = int(number) - 1
            todos = functions.get_todos()
            new_value = input("Edit it: ") + '\n'
            todos[number] = new_value.capitalize()
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue
    elif users_input.startswith("complete"):
        try:
            item = int(users_input[8:])
            item = item - 1
            todos = functions.get_todos()
            todos.pop(item)
            functions.write_todos(todos)
            print(f"You're done with {item + 1}")
        except (ValueError, IndexError):
            print("Your command is not valid")
            continue
    elif "exit" in users_input:
        print("Bye!")
        break
    else:
        print("Command is not valid")
