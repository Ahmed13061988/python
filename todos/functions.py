FILEPATH = "todos/files/todos.txt"


def get_todos(filepath=FILEPATH):
    """Get the data from a file and then store it in a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Execute this statement only when we run this file")
