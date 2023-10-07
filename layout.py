import PySimpleGUI as sg
from utils import *
from interators import *

class Layout:

    @staticmethod
    def layout():
        ARCH_NAME = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"
        
        layout = [[sg.Text('TXT Reader by: Vítor Moura and RafaelNST')],
                [sg.Button('Random choice'),
                sg.Button('Insert a name'),
                sg.Button('Remove a name'),
                sg.Button('View the content'),
                sg.Button('Exit')]]

        window = sg.Window('TXT Reader', layout)

        while True:
            event = window.read()
            if event == 'Random choice':
                sg.popup(Interators.pick_random(ARCH_NAME))
            elif event == 'Insert a name':
                sg.popup(Interators.add(ARCH_NAME))
            elif event == 'Remove a name':
                chosen = sg.popup_get_text('Enter the name to remove')
                Interators.remove(ARCH_NAME, chosen)
            elif event == 'View the content':
                sg.popup(Utils.open_file_read(ARCH_NAME))
            elif event == 'Exit' or event == sg.WIN_CLOSED:
                break
        window.close()