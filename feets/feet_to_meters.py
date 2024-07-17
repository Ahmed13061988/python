import FreeSimpleGUI as fg

convert = fg.Button("Convert")
feet_label = fg.Text("Feets")
inches_label = fg.Text("Inches")
inches = fg.Input()
feet = fg.Input()
output = fg.Text("", key="-OUTPUT-")
window = fg.Window("Convertor",
                   layout=[[feet_label, feet], [inches_label, inches], [convert, output]])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            feet = float(values[0][0])
            inches = float(values[1][0])
            meters = feet * 0.3048 + inches * 0.0254
            window['-OUTPUT-'].update(value=f"{meters}m")

        case fg.WIN_CLOSED:
            break

window.close()
