from layout import *
from utils import *

def main():
    ARCH_NAME = Functionalities.archive_name()
    window = sg.Window('TXT Reader', Popup.layout())

    while True:
        event, values = window.read()
        if event == 'Random choice':
            sg.popup(Functionalities.pick_random(ARCH_NAME))
        elif event == 'Insert a name':
            sg.popup(Functionalities.add(ARCH_NAME))
        elif event == 'Remove a name':
            chosen = sg.popup_get_text('Enter the name to remove')
            Functionalities.remove(ARCH_NAME, chosen)
        elif event == 'View the content':
            sg.popup(Tools.open_file_read(ARCH_NAME))
        elif event == 'Exit' or event == sg.WIN_CLOSED:
            break
    window.close()
    
if __name__ == "__main__":
    main()

