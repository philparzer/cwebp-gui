from webptools import grant_permission
from webptools import cwebp
from os import listdir
from os.path import isfile, join
import PySimpleGUI as sg

grant_permission() #solves no webptools permission bug


sg.theme('systemdefault')

layout = [[sg.Text('Pick a folder to batch-convert to webp', font="Helvetica 14")],
          [sg.Text('Folder', size=(8, 1), font="Helvetica 14"), sg.Input(), sg.FolderBrowse()],
          [sg.Submit()]]

window = sg.Window('Compile to webp', layout)

event, values = window.read()
window.close()#TODO: don't close on submit

print(f'You clicked on: {event}')
print(f'You chose the folder: {values[0]}')

onlyfiles = [f for f in listdir(values[0]) if isfile(join(values[0], f))]
for f in onlyfiles:
  if f.lower().endswith(('.png', '.jpg', '.jpeg')): #TODO: look into valid image file types for webptools
    print("found image: " + f)
    #TODO: add to array


#TODO: use array from above and pass each item
# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file type extension) #TODO: get relative path to images from app?
# print(cwebp(input_image="test.png", output_image="test.webp",
#             option="-q 80", logging="-v"))