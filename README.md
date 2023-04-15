# ManuCr19's Python3 Library

Una librería de Python estúpidamente simple escrita por alguien que no tiene ni idea. Espero que os sea de ayuda y sentíos libres de colaborar, gracias.

A stupidly simple Python library written by someone who doesn't have a clue. I hope you find it helpful and feel free to contribute, thanks.

## Instalar/Actualizar/Eliminar el paquete con pip
```/bin/bash
# INSTALAR
pip install pip install git+https://github.com/manucr19/library.git

# ACTUALIZAR
pip install --upgrade pip install git+https://github.com/manucr19/library.git

# ELIMINAR
pip unistall manucr19_py
```

## manucr19-py/file.py
Archivo de funciones para trabajar con ficheros en phyton:
  - file.cat: Muestra el contenido de un fichero por pantalla.
  - file.create: Crea un fichero con un texto.
  - file.delete: Elimina un fichero.
  - file.replace_text: Cambia un texto por otro en un fichero.
  - file.add_text: Añade un texto al final de un fichero.

## manucr19-py/tui.py
Archivo de funciones que utiliza la libreria pythondialog para crear interfaces de usuario de texto.
  - tui.msgbox: Muestra una ventana de mensaje con título y texto personalizados
  - tui.yesno: Muestra una ventana con opciones de sí/no, con título y texto personalizados
  - tui.imputbox: Muestra una ventana con un campo de entrada de texto, con título y texto personalizados
  - tui.menu: Muestra una ventana con una lista de opciones, con título y texto personalizados
  - tui.infobox: Muestra una ventana con información en formato de caja, con título y texto personalizados
