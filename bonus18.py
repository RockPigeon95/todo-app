import PySimpleGUI as sg
import extract

archive_label = sg.Text("Select Archive:")
archive_path = sg.Input(tooltip='Select Archive')
archive_button = sg.FileBrowse("Choose", key='archive')

destination_label = sg.Text("Select Destination:")
destination_path = sg.Input(tooltip='Select Destination')
destination_button = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='Green')

window = sg.Window("File Extractor",
                   layout=[[archive_label, archive_path, archive_button],
                           [destination_label, destination_path, destination_button],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    file_path = values['archive']
    dest_path = values['folder']
    extract.extract_archive(file_path, dest_path)
    window['output'].update("Files extracted successfully!")
    match event:
        case sg.WINDOW_CLOSED:
            break

window.close()
