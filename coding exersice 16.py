import PySimpleGUI as sg
import converter

sg.theme('Black')
feet_label = sg.Text("Enter feet:")
feet_box = sg.InputText(key='feet')

inches_label = sg.Text("Enter inches:")
inches_box = sg.InputText(key='inches')

convert_button = sg.Button("Convert")
meters_label = sg.Text(key='meters')
exit_button = sg.Button("Exit")

window = sg.Window("Imperial to Metric Converter", layout=[[feet_label, feet_box],
                                                           [inches_label, inches_box],
                                                           [convert_button, exit_button, meters_label]])
while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                meters = converter.convert(feet, inches)
                window['meters'].update(f"{meters}m")
            except ValueError:
                sg.popup("Please enter values to convert!")
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break
window.close()
