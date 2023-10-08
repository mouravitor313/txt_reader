import PySimpleGUI as sg
from random import choice

class Tools:
    def __init__(self):
        self
        
    @staticmethod
    def open_file_read(arch_name):
        with open(arch_name) as archive:
            return archive.read()
        
    def open_file_readlines(arch_name):
        with open(arch_name) as archive:
            return archive.readlines()
        
class Functionalities:
    def __init__(self):
        self

    def archive_name() -> str:
        while True:
            ARCH_NAME = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"

            if ARCH_NAME == "":
                sg.popup("Invalid archive name")
                
            else:
                return ARCH_NAME
    
    def add(arch_name):
        add_name_popup = sg.popup_get_text("Enter a student's name").strip()

        if not arch_name == "":

            if not add_name_popup == "":
                with open(arch_name, 'a') as archive:
                    return archive.write(f'\n{add_name_popup}')
                
            else:
                sg.popup("Valid name required")

        else:
            with open(arch_name, 'a') as archive:
                return archive.write(f'\n{add_name_popup}')

    def pick_random(arch_name):
        names = Tools.open_file_readlines(arch_name)

        return choice(names).strip()

    def remove(arch_name, chosen):
        rows = Tools.open_file_readlines(arch_name)

        if not chosen == "":
            rows = [name.strip() for name in rows if name.strip() != chosen]

        else:
            sg.popup("Enter a valid name")

        with open(arch_name, 'w') as archive:
                for name in rows:
                    if rows.index(name) == len(rows)-1:
                        archive.write(name)

                    else:
                        archive.write(name + '\n')

