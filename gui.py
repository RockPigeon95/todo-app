import functions
import PySimpleGUI as sg

label = sg.Text("Type In a To-Do: ")
inputBox = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [inputBox, add_button]])

window.read()
window.close()
