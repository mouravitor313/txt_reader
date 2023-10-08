import PySimpleGUI as sg
from random import choice

class Tools:
    def open_file_read(arch_name):
        with open(arch_name) as archive:
            return archive.read()
        
    def open_file_readlines(arch_name):
        with open(arch_name) as archive:
            return archive.readlines()
    
    def archive_name() -> str:
        "Ask the archive file name to the user"
        while True:
            ARCH_NAME = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"

            if ARCH_NAME == ".txt":
                sg.popup("Invalid archive name")
            else:
                return ARCH_NAME
        
class Functionalities:
    def add(arch_name, add_name_popup):
        "Add a word to a txt file"
        with open(arch_name, 'a') as archive:
            if not arch_name == "":
                if not add_name_popup == "":
                        archive.write(f'\n{add_name_popup}')
                else:
                    sg.popup("Valid name required")
            else:
                return archive.write(f'\n{add_name_popup}')

    def pick_random(arch_name):
        "Pick a random word from a txt file"

        names = Tools.open_file_readlines(arch_name)
        return choice(names).strip()

    def remove(arch_name, chosen) -> None:
        "Remove a row from a txt file"

        rows = Tools.open_file_readlines(arch_name)

        # Rows and input treatment
        if not chosen.strip() == "":
            # Add every word, not being the chosen one, to 'rows'
            rows = [name.strip() for name in rows if name.strip() != chosen]

            # File writing
            with open(arch_name, 'w') as archive:
                for name in rows:
                    if rows.index(name) == len(rows)-1:
                        archive.write(name)
                    else:
                        archive.write(name + '\n')
        else:
            sg.popup("Enter a valid name")

