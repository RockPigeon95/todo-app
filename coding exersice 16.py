import PySimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_box = sg.InputText()

inches_label = sg.Text("Enter inches:")
inches_box = sg.InputText()

convert_button = sg.Button("Convert")

window = sg.Window("Imperial to Metric Converter", layout=[[feet_label, feet_box],
                                                           [inches_label, inches_box],
                                                           [convert_button]])
window.read()
window.close()
