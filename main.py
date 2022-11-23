from webptools import grant_permission
from webptools import cwebp

grant_permission()
# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file type extension)
# print(cwebp(input_image="test.png", output_image="test.webp",
#             option="-q 80", logging="-v"))

import PySimpleGUI as sg

sg.theme('systemdefault')

layout = [[sg.Text('Pick a folder to batch-convert to webp', font="Helvetica 14")],
          [sg.Text('Folder', size=(8, 1), font="Helvetica 14"), sg.Input(), sg.FolderBrowse()],
          [sg.Submit()]]

window = sg.Window('Compile to webp', layout)

event, values = window.read()
window.close()
print(f'You clicked on: {event}')
print(f'You chose the folder: {values[0]}')