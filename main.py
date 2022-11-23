from webptools import grant_permission
from webptools import cwebp
from os import listdir
from os.path import isfile, join, relpath, curdir
import PySimpleGUI as sg

grant_permission() #solves no webptools permission bug


sg.theme('systemdefault')

layout = [[sg.Text('Pick a folder to batch-convert to webp', font="Helvetica 14")], #TODO: style
          [sg.Text('Folder', size=(8, 1), font="Helvetica 14"), sg.Input(), sg.FolderBrowse()],
          [sg.Submit()]]

window = sg.Window('Compile to webp', layout)

event, values = window.read()
window.close()#TODO: don't close on submit

onlyfiles = [f for f in listdir(values[0]) if isfile(join(values[0], f))]
for f in onlyfiles:
  if f.lower().endswith(('.png', '.jpg', '.jpeg')): #TODO: look into valid image file types for webptools
    path = relpath(join(values[0], f), start = curdir) 
    
    #TODO: create option input field to set quality
    #TODO: strip file extension and replace with webp
    cwebp(input_image=path, output_image=f'{path}.webp', option="-q 80", logging="-v") 
    
  #TODO: raise something if no images found