import FreeSimpleGUI as fs
import functions

label = fs.Text("Type a to-do")
input_box = fs.InputText(tooltip="Enter todo", key="todo")
button = fs.Submit("Add")
window = fs.Window("To do App",
                   layout=[[label], [input_box, button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    todo_list = functions.get_todos()
    match event:
        case "Add":
            todo_list.append(values["todo"] + "\n")
            functions.write_todos(todo_list)
        case fs.WIN_CLOSED:
            break
print(todo_list)





window.close()
