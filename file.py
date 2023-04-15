from subprocess import run

def cat(file):
    # Muestra por pantalla el contenido del fichero 'file'
    #
    # file: str - Ruta del fichero (Ej:"/ruta/ejemplo")
    #
    f = open(file,"r")
    txt = f.read()
    print(txt)
    f.close()

def create(file,txt):
    # Crea o sobreescribe el fichero 'file' con el string 'txt'
    #
    # file: str - Ruta del fichero (Ej:"/ruta/ejemplo.txt")
    # txt: str - Contenido que se escribirá en el fichero
    #
    f = open(file,"w")
    f.write(txt)
    f.close()

def delete(file):
    # Elimina el fichero 'file'
    #
    # file: str - Ruta del fichero (Ej:"/ruta/ejemplo.txt")
    #
    run(["rm","-f",file])

def replace_text(file,str1,str2):
    # Remplaza las apariciones del texto 'str1' por el texto 'str2' en el fichero 'file'
    #
    # file: str - Ruta del fichero (Ej:"/ruta/ejemplo.txt")
    # str1: str - Texto original que será reemplazado
    # str2: str - Texto nuevo que reemplazará al texto original
    #
    f = open(file,"r")
    txt = f.read()
    txt = txt.replace(str1,str2)
    f.close()
    f = open(file,"w")
    f.write(txt)
    f.close()

def add_text(file,txt):
    # Añade el texto 'txt' al final del fichero 'file'
    #
    # file: str - Ruta del fichero (Ej:"/ruta/ejemplo.txt")
    # txt: str - Contenido que se añadirá al final del fichero
    #
    f = open(file,"a")
    f.write("\n" + txt)
    f.close()

