import PySimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_box = sg.InputText(key='feet')

inches_label = sg.Text("Enter inches:")
inches_box = sg.InputText(key='inches')

convert_button = sg.Button("Convert")
meters_label = sg.Text(key='meters')

window = sg.Window("Imperial to Metric Converter", layout=[[feet_label, feet_box],
                                                           [inches_label, inches_box],
                                                           [convert_button, meters_label]])
while True:
    event, values = window.read()
    print(event, values)
    feet = float(values['feet'])
    inches = float(values['inches'])
    meters = (feet * 30.48)/100 + (inches * 2.54)/100
    window['meters'].update(f"{meters}m")

window.close()
