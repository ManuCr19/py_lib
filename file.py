def cat(file):
    # 'file': "/ruta/ejemplo.txt"
    # Muestra por pantalla el contenido del fichero 'file'
    f = open(file,"r")
    txt = f.read()
    print(txt)
    f.close()

def create(file,txt):
    # 'file': "/ruta/ejemplo.txt"
    # 'txt': "Texto de ejemplo"
    # Crea o sobreescribe el fichero 'file' con el string 'txt'
    f = open(file,"w")
    f.write(txt)
    f.close()

def delete(file):
    # 'file': "/ruta/ejemplo.txt"
    # Elimina el fichero 'file'
    from os import remove
    remove(file)

def replace_text(file,str1,str2):
    # 'file': "/ruta/ejemplo.txt"
    # 'str1': "Texto de ejemplo"
    # 'str2': "Texto de ejemplo"
    # Remplaza las apariciones del texto 'str1' por el texto 'str2' en el fichero 'file'
    f = open(file,"r")
    txt = f.read()
    txt = txt.replace(str1,str2)
    f.close()
    f = open(file,"w")
    f.write(txt)
    f.close()

def add_text(file,txt):
    # 'file': "/ruta/ejemplo.txt"
    # 'txt': "Texto de ejemplo"
    # Añade el texto 'txt' al final del fichero 'file'
    f = open(file,"a")
    f.write("\n" + txt)
    f.close()
