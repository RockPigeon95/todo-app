import PySimpleGUI as sg
import zip

target_file_label = sg.Text("Select files to compress:")
destination_label = sg.Text("Select destination folder:")

target_file_box = sg.InputText(tooltip="Select File")
destination_box = sg.InputText(tooltip="Select Destination")

target_button = sg.FilesBrowse("Choose", key='files')
destination_button = sg.FolderBrowse("Choose", key='folder')
compress_button = sg.Button("Compress")
output = sg.Text(key='output', text_color='green')

window = sg.Window("File Compressor", layout=[[target_file_label, target_file_box, target_button],
                                              [destination_label, destination_box, destination_button],
                                              [compress_button, output]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder_path = values['folder']
    zip.make_archive(filepaths, folder_path)
    window['output'].update("Files compressed successfully!")

window.close()
