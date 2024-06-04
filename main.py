todos = []

while True:
    users_input = input("Type add or show: ")
    match users_input:
        case "add":
            todo = input("Enter the todo: ")
            todos.append(todo.capitalize())
        case "show":
            print(todos)



