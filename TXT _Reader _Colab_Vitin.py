import PySimpleGUI as sg
from random import choice
from os import system

def open_file(arch_name):
    with open(arch_name) as archive:
        rows = archive.read()
    return rows

def add(arch_name):
    add_name_popup = sg.popup_get_text("Enter a student's name").strip()
    sg.popup(add_name_popup)
    with open(arch_name, 'a') as archive:
        added_name = archive.write(f'\n{add_name_popup}')
    return added_name

def pick_random(arch_name):
    with open(arch_name) as archive:
        names = archive.readlines()
        return choice(names).strip()

def remove(arch_name, chosen):
    with open(arch_name) as archive:
        rows = archive.readlines()
        rows = [name.strip() for name in rows if name.strip() != chosen]
      
    with open(arch_name, 'w') as archive:
        for name in rows:
            if rows.index(name) == len(rows)-1:
                archive.write(name)
            else:
                archive.write(name + '\n')

def main():
    arch_name = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"
    
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
            sg.popup(pick_random(arch_name))
        elif event == 'Insert a name':
            sg.popup(add(arch_name))
        elif event == 'Remove a name':
            chosen = sg.popup_get_text('Enter the name to remove')
            if not chosen == None or chosen == "":
                remove(arch_name, chosen)
        elif event == 'View the content':
            sg.popup(open_file(arch_name))
        elif event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
