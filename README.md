# ManuCr19's Python3 Library

A stupidly simple Python library written by someone who doesn't have a clue. I hope you find it helpful and feel free to contribute, thanks.

## Install/Update/Uninstall the package with pip
```/bin/bash
# INSTALL
pip install git+https://github.com/manucr19/py_lib.git

# UPDATE
pip install --upgrade git+https://github.com/manucr19/py_lib.git

# UNINSTALL
pip unistall manucr19_py_lib
```

## manucr19_py_lib/file.py
File containing functions for working with files in Python:
  - `file.cat`: Displays the content of a file on the screen.
  - `file.create`: Creates a file with specified text.
  - `file.delete`: Deletes a file.
  - `file.replace_text`: Replaces one text with another in a file.
  - `file.add_text`: Appends text to the end of a file.

## manucr19_py_lib/tui.py
File containing functions that use the pythondialog library to create text user interfaces.
  - `tui.msgbox`: Displays a message window with custom title and text.
  - `tui.yesno`: Displays a window with yes/no options, with custom title and text.
  - `tui.inputbox`: Displays a window with a text input field, with custom title and text.
  - `tui.menu`: Displays a window with a list of options, with custom title and text.
  - `tui.infobox`: Displays a window with information in box format, with custom title and text.
