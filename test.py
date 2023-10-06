from utils import *
import PySimpleGUI as sg
from random import choice
from os import system

def add(arch_name):
    add_name_popup = sg.popup_get_text("Enter a student's name").strip()
    if not arch_name == "":
        if not add_name_popup == "":
            with open(arch_name, 'a') as archive:
                return archive.write(add_name_popup)
        else:
            sg.popup("Valid name required")
    else:
        with open(arch_name, 'a') as archive:
            return archive.write('\n' + add_name_popup)

def pick_random(arch_name):
    names = open_file_read(arch_name)
    return choice(names).strip()

def remove(arch_name, chosen):
    rows = open_file_readlines(arch_name)

    if not chosen == "":
        for name in rows:
            if name.strip() != chosen:
                rows.append(name.strip())
    else:
        sg.popup("Enter a valid name")

    for name in rows:
        if rows.index(name) == len(rows)-1:
            with open(arch_name, 'w') as archive:
                archive.write(name)
        else:
            with open(arch_name, 'w') as archive:
                archive.write(name + '\n')

def main():
    ARCH_NAME = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"
    
    layout = [[sg.Text('TXT Reader by: Vítor Moura and RafaelNST')],
              [sg.Button('Random choice'),
               sg.Button('Insert a name'),
               sg.Button('Remove a name'),
               sg.Button('View the content'),
               sg.Button('Exit')]]

    window = sg.Window('TXT Reader', layout)

    while True:
        event, values = window.read()

        if event == 'Random choice':
            sg.popup(pick_random(ARCH_NAME))
        elif event == 'Insert a name':
            sg.popup(add(ARCH_NAME))
        elif event == 'Remove a name':
            chosen = sg.popup_get_text('Enter the name to remove')
            remove(ARCH_NAME, chosen)
        elif event == 'View the content':
            sg.popup(open_file_read(ARCH_NAME))
        elif event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
