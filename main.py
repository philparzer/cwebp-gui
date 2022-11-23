from webptools import grant_permission
from webptools import cwebp
from os import listdir
from os.path import isfile, join, relpath, curdir
import PySimpleGUI as sg

#if os restricts webptools permission
grant_permission() 

#GUI
sg.theme('systemdefault')

layout = [
          [sg.Text('Image Folder', font="Helvetica 14"), sg.Input(key="-PATH-"), sg.FolderBrowse(font="Helvetica 14")],
          [sg.Text('Compression', font="Helvetica 14"), sg.Input(key="-COMPRESSION_RATE-", font="Helvetica 14", size=(4,1), tooltip="n most recent tweets to be scraped", default_text="80"),sg.Text('%', font="Helvetica 14")],
          [sg.Button('Start', font="Helvetica 14", pad=((5,5),(20,0)), button_color="green")],
          [sg.Text('Status', key='-STATUS-', pad=((5,0),(5,0)), font="Helvetica 10")]
        ]
          

window = sg.Window('Compile to webp', layout)

while True:

  event, values = window.read()

  if event == 'Start':
    try:
      compression_rate = int(values['-COMPRESSION_RATE-'])
      if (compression_rate < 0 or compression_rate > 100): 
        window['-STATUS-'].update('Enter an integer between 0-100', text_color='red')
        continue

    except Exception as e:
      window['-STATUS-'].update('Enter a valid integer', text_color='red')
      continue

    if values["-PATH-"] == '':
        window['-STATUS-'].update('Pick a folder', text_color='red')
        continue

    #cwebp
    onlyfiles = [f for f in listdir(values["-PATH-"]) if isfile(join(values["-PATH-"], f))]
    converted_images = 0
    compression_rate
    for f in onlyfiles:
      if f.lower().endswith(('.png', '.jpg', '.jpeg')): #TODO: look into valid image file types for webptools
        path = relpath(join(values["-PATH-"], f), start = curdir) 
        #TODO: use os.splitext
        #TODO: create option input field to set quality
        #TODO: strip file extension and replace with webp
        cwebp(input_image=path, output_image=f'{path}.webp', option=f"-q {values['-COMPRESSION_RATE-']}", logging="-v") 
        converted_images += 1

    else:
      if(converted_images > 0): window["-STATUS-"].update(f"Converted {converted_images} images", text_color='green')
      else: window["-STATUS-"].update("Found no valid images to convert", text_color='yellow')
  if event == sg.WIN_CLOSED or event == 'Exit':
    break


window.close()
quit() #FIXME: when compiled