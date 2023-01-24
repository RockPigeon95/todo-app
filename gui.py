import functions
import PySimpleGUI as sg

label = sg.Text("Type In a To-Do: ")
inputBox = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
todo_list = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[40,10])
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [inputBox, add_button],
                           [todo_list, edit_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
