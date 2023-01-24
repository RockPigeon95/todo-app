import functions
import PySimpleGUI as sg

label = sg.Text("Type In a To-Do: ")
inputBox = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
window = sg.Window("My To-Do App",
                   layout=[[label], [inputBox, add_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
