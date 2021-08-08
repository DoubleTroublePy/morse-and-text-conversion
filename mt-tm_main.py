from PySimpleGUI.PySimpleGUI import No
from vocabolary import vocabolary  
from conversion import conversion
import PySimpleGUI as sg
import re

Diz = conversion()

def defaultWindow():
    mt = 'morse to text'
    tm = 'text to morse'
    lenght = 500
    height = 470
    value = [mt, tm]
    layout = [  #define the layout 
                [sg.Text("direction of the conversion")],
                [sg.Combo(value, size=(lenght, 10), enable_events=True, key='-INPUT-')],
                [sg.Text("text to convert")],
                [sg.Multiline(size = (lenght, 10), key='-value-')], 
                [sg.Multiline(size=(lenght, 10), key='-OUTPUT-')],  
                [sg.Button('Ok', size = (5, 1)), sg.Button('Quit', size = (5, 1))]]
    
    # Create the window
    window = sg.Window('Conversione', layout, size = (lenght, height))      

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window 
        if event == 'Ok':
            window['-OUTPUT-'].update(None)
            input = values['-INPUT-']

            #text to morse
            if input == 'text to morse':
                find = re.search(r'[^A-Za-z0-9]', str(values['-value-']))
                find_group = find.group()
                if value == "" and find_group != ['\n'] and len(find_group) != len(values['-value-']):
                    window.FindElement('-value-').Update('') #warning popup if a wrong charatter is inseted
                    sg.PopupAutoClose  (
                    "Warning erroneous input",
                    non_blocking=False,
                    )
                    window['-value-'].update(None)
                else:
                    value = Diz.txtMs(str(values['-value-'])) #conversion text morse

            #morse to text
            elif input == 'morse to text':
                #make sure that in the morse there is only allow char and avoid conversion error
                if value == "" or re.findall(r'[a-zA-Z]', str(values['-value-'])) != [] :
                    window.FindElement('-value-').Update('') #warning popup if a wrong charatter is inseted
                    sg.PopupAutoClose  (
                    "Warning erroneous input",
                    non_blocking=False, 
                    )
                    window['-value-'].update(None)
                else:
                    value = Diz.msTxt(values['-value-'])
            if value != [mt, tm]:
                window['-OUTPUT-'].update(value) #conversion morse text

if __name__ == '__main__':
    defaultWindow()

# ==============================================================================================================================================                                                    
# |                                                                                         | Double Trouble                                   |
# |                                           #                                             |     project: morse and text conversion           |
# |                                          ###                                            |     date: 2021-08-08                             |
# |                                         #####                                           |     file description:                            |
# |                     ############        #####        ###########                        |       this is the main file and the majority     |
# |               ######################   #######   #########################              |       of code handle graphics there is only      |
# |           ####################################################################          |       a little bit of sting controll and         |
# |       ############################################################################      |       manipulation                               |
# |    #################################################################################    |                                                  |
# |            ######   #################  #######  #################   #######             |                                                  |
# |                                         #####                                           |--------------------------------------------------|
# |                                         #####                                           | Social                                           |
# |                                        #######                                          |     Github: http://github.com/DoubleTroublePy    |
# |                                       #########                                         |     Twitter: @DoubleTroublePy                    |
# |                                                                                         |                                                  |
# ==============================================================================================================================================