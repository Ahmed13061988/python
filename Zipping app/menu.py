import FreeSimpleGUI as fs

label1 = fs.Text("Select files to compress")
button1 = fs.FileBrowse("Choose")
input_text1 = fs.Input()
input_text2 = fs.Input()
label2 = fs.Text("Select destination folder")
button2 = fs.FolderBrowse("Choose")
submit_button = fs.Button("Compress")
window = fs.Window("File Zipper",
                   layout=[[label1, input_text1, button1], [label2, input_text2, button2], [submit_button]])
window.BackgroundColor = "black"
window.read()
window.close()
