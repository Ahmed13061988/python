import FreeSimpleGUI as fs
import functions

label = fs.Text("Type a to-do")
input_box = fs.InputText()
button = fs.Submit("Add")
window = fs.Window("To do App", layout=[[label], [input_box, button]])
window.read()
window.close()
