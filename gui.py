import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open("todos.txt", 'w') as file:
        pass

sg.theme('LightBrown8')
clock = sg.Text('', key='clock')
label = sg.Text("Type In a To-Do: ")
inputBox = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
todo_list = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(40, 10))
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [inputBox, add_button],
                           [todo_list, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y - %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select a todo to edit!", font=('Helvetica', 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select a todo to edit!", font=('Helvetica', 15))
        case 'Exit':
            break
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("Enter a todo first!")
        case sg.WINDOW_CLOSED:
            break

window.close()
