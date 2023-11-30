"""File containing functions that use pythondialog to create text interfaces"""

import sys
from subprocess import run
from dialog import Dialog

# Checking that the 'dialog' command is installed on the system
output = run(["which","dialog"], capture_output=True, check=False)
if output.returncode != 0:
    print("The 'dialog' command is not installed, it is necessary")
    sys.exit()

def msgbox(title, text, height = None, width = None):
    """
    Displays a message window with custom title and text

    title: str - Text to be displayed as the window title
    text: str - Text to be displayed in the window content
    height: int (optional) - Number of pixels to define the height of the window
    width: int (optional) - Number of pixels to define the width of the window
    """
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.msgbox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear", check=False)
        sys.exit()

def yesno(title, text, height = None, width = None):
    """
    Displays a window with yes/no options, with custom title and text

    title: str - Text to be displayed as the window title
    text: str - Text to be displayed in the window content
    height: int (optional) - Number of pixels to define the height of the window
    width: int (optional) - Number of pixels to define the width of the window

    returns: bool - True if the user selects "Yes," False if they select "No"
    """
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.yesno(text, title = title, height = height, width = width)
    if code == d.OK:
        return True
    if code == d.CANCEL:
        return False
    if code == d.ESC:
        run("clear", check=False)
        sys.exit()
    return None

def inputbox(title, text, init = "", height = None, width = None):
    """
    Displays a window with a text input field, with custom title and text
   
    title: str - Text to be displayed as the window title
    text: str - Text to be displayed in the window content
    init: str (optional) - Text to be displayed as the initial value of the text input field
    height: int (optional) - Number of pixels to define the height of the window
    width: int (optional) - Number of pixels to define the width of the window
   
    returns: str - Text entered by the user
    """
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, string = d.inputbox(text, init = init, title = title, height = height, width = width)
    if code == d.OK:
        return string
    if code == d.CANCEL:
        run("clear", check=False)
        sys.exit()
    if code == d.ESC:
        run("clear", check=False)
        sys.exit()
    return None

def menu(title, text, choices, height = None, width = None):
    """
    Displays a window with a list of options, with custom title and text
   
    title: str - Text to be displayed as the window title
    text: str - Text to be displayed in the window content
    choices: list of tuples - List of options as tuples (tag, description)
        - Example: [("1.", "Option 1"), ("2.", "Option 2")]
    height: int (optional) - Number of pixels to define the height of the window
    width: int (optional) - Number of pixels to define the width of the window
   
    returns: str - The tag of the option selected by the user (For example: "1." or "2.")
    """
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, tag = d.menu(text, choices = choices, title = title, height = height, width = width)
    if code == d.OK:
        return tag
    if code == d.CANCEL:
        run("clear", check=False)
        sys.exit()
    if code == d.ESC:
        run("clear", check=False)
        sys.exit()
    return None

def infobox(title, text, height = None, width = None):
    """
    Displays a window with information in box format, with custom title and text
   
    title: str - Text to be displayed as the window title
    text: str - Text to be displayed in the window content
    height: int (optional) - Number of pixels to define the height of the window
    width: int (optional) - Number of pixels to define the width of the window
    """
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.infobox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear", check=False)
        sys.exit()
