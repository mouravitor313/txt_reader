import PySimpleGUI as sg
from random import choice
from os import system

def get_file_name():
    name = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"
    return name

def open_file(name):
    with open(name) as archive:
        names = archive.read()
    return names

def add(name):
    additional = sg.popup_get_text("Enter a student's name").strip()
    sg.popup(additional)
    with open(name, 'a') as archive:
        update = archive.write(f'{additional}\n')
    return update

def pick_random(name):
    with open(name) as archive:
        names = archive.readlines()
        return choice(names).strip()

def remove(name, chosen):
    with open(name) as archive:
        names = archive.readlines()
        names = [i.strip() for i in names if i.strip() != chosen]
      
    with open(name, 'w') as archive:
        for i in names:
            if names.index(i) == len(names)-1:
                archive.write(i)
            else:
                archive.write(i + '\n')

def main():
    layout = [[sg.Text('TXT Reader by: Vítor Moura and RafaelNST')],
              [sg.Button('Random choice'),
               sg.Button('Insert a name'),
               sg.Button('Remove a name'),
               sg.Button('View the content'),
               sg.Button('Exit')]]

    window = sg.Window('TXT Reader', layout)

    while True:
        event, values = window.read()

        name = sg.popup_get_text(get_file_name())

        if event == 'Random choice':
            sg.popup(pick_random(name))
        elif event == 'Insert a name':
            sg.popup(add(name))
        elif event == 'Remove a name':
            chosen = sg.popup_get_text('Enter the name to remove')
            if not chosen == None or chosen == "":
                remove(name, chosen)
        elif event == 'View the content':
            sg.popup(open_file(name))
        elif event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
