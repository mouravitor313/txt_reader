import PySimpleGUI as sg
from random import choice
from os import system

def get_file_name():
    name = sg.popup_get_text('Enter the archive name').strip()
    name += '.txt'
    return name

def open_file(name):
    with open(name) as archive:
        students = archive.read()
    return students

def add(name):
    additional = sg.popup_get_text('Enter a student\'s name').replace(" ", "")
    with open(name, 'a') as archive:
        update = archive.write(f'\n{additional}')
    return update

def pick_random(name):
    with open(name) as archive:
        names = archive.readlines()
        return choice(names).strip()

def remove(name, chosen):
    with open(name) as archive:
        rows = list()
        rows = archive.readlines()
        rows = [i.strip() for i in rows if i.strip() != chosen]
      
    with open(name, 'w') as archive:
        for name in rows:
            if rows.index(name) == len(rows)-1:
                archive.write(name)
            else:
                archive.write(name + '\n')

def main():
    layout = [[sg.Text('TXT Reader by: Vítor Moura and RafaelNST')],
              [sg.Button('Insert the archive\'s name'),
               sg.Button('Random choice'),
               sg.Button('Insert a name'),
               sg.Button('Remove a name'),
               sg.Button('View the content'),
               sg.Button('Exit')]]

    window = sg.Window('TXT Reader', layout)

    while True:
        event, values = window.read()
        if event == "Insert the archive's name":
            name = sg.popup(get_file_name())
        elif event == 'Random choice':
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
