"""Functions for working with files in Python"""

from subprocess import run

def cat(file_path):
    """
    Displays the content of the 'file' on the screen

    file: str - Path of the file (e.g., "/path/example")
    """
    with open(file_path, "r", encoding="utf-8") as f:
        txt = f.read()
        print(txt)

def create(file_path, txt):
    """
    Creates or overwrites the 'file' with the string 'txt'

    file: str - Path of the file (e.g., "/path/example.txt")
    txt: str - Content to be written to the file
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(txt)

def delete(file):
    """
    Deletes the 'file'

    file: str - Path of the file (e.g., "/path/example.txt")
    """
    run(["rm", "-f", file], check=False)

def replace_text(file_path, str1, str2):
    """
    Replaces occurrences of the text 'str1' with the text 'str2' in the 'file'

    file: str - Path of the file (e.g., "/path/example.txt")
    str1: str - Original text to be replaced
    str2: str - New text to replace the original text
    """
    with open(file_path, "w", encoding="utf-8") as f:
        txt = f.read()
        txt = txt.replace(str1,str2)
        f.write(txt)

def add_text(file_path, txt):
    """
    Adds the text 'txt' to the end of the 'file'

    file: str - Path of the file (e.g., "/path/example.txt")
    txt: str - Content to be added to the end of the file
    """
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + txt)
