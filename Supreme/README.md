# TXT Reader

TXT Reader is a Python project that uses the PySimpleGUI library to create a graphical user interface (GUI) for managing text files. It allows the user to add, remove, view, and pick random words from a text file.

## Installation

To run this project, you need to have Python 3 and PySimpleGUI installed on your system. You can install PySimpleGUI using pip:

\```bash
pip install PySimpleGUI
\```

## Usage

To start the project, run the `main.py` script:

\```bash
python main.py
\```

This will open a window with five buttons:

- Random choice: This will pick a random word from the text file and display it in a popup.
- Insert a name: This will ask the user to enter a word and add it to the text file.
- Remove a name: This will ask the user to enter a word and remove it from the text file.
- View the content: This will show the content of the text file in a popup.
- Exit: This will close the window and exit the program.

The text file name is specified by the user when the program starts. The default text file name is `alunos.txt`.

## Modules

The project consists of three modules:

- `main.py`: This is the main script that creates and runs the GUI window.
- `layout.py`: This contains the `Popup` class that defines the layout of the GUI window.
- `utils.py`: This contains the `Tools` and `Functionalities` classes that provide various methods for working with text files.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
