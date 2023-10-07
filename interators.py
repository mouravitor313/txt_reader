from random import choice
from utils import *
import PySimpleGUI as sg

class Interators:
    def __init__(self) -> None:
        pass

    @staticmethod
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

    @staticmethod
    def pick_random(arch_name):
        names = Utils.open_file_read(arch_name)
        return choice(names).strip()

    @staticmethod
    def remove(arch_name, chosen):
        rows = Utils.open_file_readlines(arch_name)

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
