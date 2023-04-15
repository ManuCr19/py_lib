from dialog import Dialog
from subprocess import run

# Comprobacion de que el comando 'dialog' esta instalado en el sistema
if subprocess.run(["which","dialog"]) != 0:
    print("Es necesario disponer del comando 'dialog' instalado en el sistema para utilizar esta funcionalidad")
    exit()

def msgbox(title, text, height = None, width = None):
    # Muestra una ventana de mensaje con título y texto personalizados
    #
    # title: str - Texto que se mostrará como título de la ventana
    # text: str - Texto que se mostrará en el contenido de la ventana
    # height: int (opcional) - Número de píxeles para definir la altura de la ventana
    # width: int (opcional) - Número de píxeles para definir el ancho de la ventana
    #
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.msgbox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear")
        exit()

def yesno(title, text, height = None, width = None):
    # Muestra una ventana con opciones de sí/no, con título y texto personalizados
    #
    # title: str - Texto que se mostrará como título de la ventana
    # text: str - Texto que se mostrará en el contenido de la ventana
    # height: int (opcional) - Número de píxeles para definir la altura de la ventana
    # width: int (opcional) - Número de píxeles para definir el ancho de la ventana
    #
    # returns: bool - True si el usuario selecciona "Sí", False si selecciona "No"
    #
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.yesno(text, title = title, height = height, width = width)
    if code == d.OK:
        return True
    elif code == d.CANCEL:
        return False
    elif code == d.ESC:
        run("clear")
        exit()

def inputbox(title, text, init = "", height = None, width = None):
    # Muestra una ventana con un campo de entrada de texto, con título y texto personalizados
    #
    # title: str - Texto que se mostrará como título de la ventana
    # text: str - Texto que se mostrará en el contenido de la ventana
    # init: str (opcional) - Texto que se mostrará como valor inicial del campo de entrada de texto
    # height: int (opcional) - Número de píxeles para definir la altura de la ventana
    # width: int (opcional) - Número de píxeles para definir el ancho de la ventana
    #
    # returns: str - Texto ingresado por el usuario
    #
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, string = d.inputbox(text, init = init, title = title, height = height, width = width)
    if code == d.OK:
        return string
    elif code == d.CANCEL:
        run("clear")
        exit()
    elif code == d.ESC:
        run("clear")
        exit()

def menu(title, text, choices, height = None, width = None):
    # Muestra una ventana con una lista de opciones, con título y texto personalizados
    #
    # title: str - Texto que se mostrará como título de la ventana
    # text: str - Texto que se mostrará en el contenido de la ventana
    # choices: list of tuples - Lista de opciones como tuplas (tag, descripción)
    #                            Ejemplo: [("1.", "Opción 1"), ("2.", "Opción 2")]
    # height: int (opcional) - Número de píxeles para definir la altura de la ventana
    # width: int (opcional) - Número de píxeles para definir el ancho de la ventana
    #
    # returns: str - El tag de la opción seleccionada por el usuario (Por ejemplo: "1." O "2.")
    #
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, tag = d.menu(text, choices = choices, title = title, height = height, width = width)
    if code == d.OK:
        return tag
    elif code == d.CANCEL:
        run("clear")
        exit()
    elif code == d.ESC:
        run("clear")
        exit()

def infobox(title, text, height = None, width = None):
    # Muestra una ventana con información en formato de caja, con título y texto personalizados
    #
    # title: str - Texto que se mostrará como título de la ventana
    # text: str - Texto que se mostrará en el contenido de la ventana
    # height: int (opcional) - Número de píxeles para definir la altura de la ventana
    # width: int (opcional) - Número de píxeles para definir el ancho de la ventana
    #
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.infobox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear")
        exit()
