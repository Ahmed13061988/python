import FreeSimpleGUI as fs
import functions

label = fs.Text("Type a to-do")
input_box = fs.InputText(tooltip="Enter todo", key="todo")
list_box = fs.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
button = fs.Button("Add")
edit = fs.Button("Edit")
close = fs.Button("Close")
complete = fs.Button("Completed")
window = fs.Window("To do App",
                   layout=[[label], [input_box, button], [list_box, edit, complete], [close]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    todo_list = functions.get_todos()
    print(event, values)
    match event:
        case "Add":
            todo_list.append(values["todo"] + "\n")
            functions.write_todos(todo_list)
            window["todos"].update(values=todo_list)
        case "Edit":
            for i in range(len(todo_list)):
                if todo_list[i] == values["todos"][0]:
                    todo_list[i] = (values["todo"] + "\n").capitalize()
            functions.write_todos(todo_list)
            window["todos"].update(values=todo_list)
        case "Completed":
            if values["todos"][0] in todo_list:
                todo_list.remove(values["todos"][0])
            functions.write_todos(todo_list)
            window["todos"].update(values=todo_list)
        case "Close":
            window.close()
        case fs.WIN_CLOSED:
            break
print(todo_list)

window.close()
