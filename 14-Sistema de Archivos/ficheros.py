from asyncore import read
from io import open
import pathlib 
import shutil
import os
import os.path

#Abrir un archivo
archivo = open(str(pathlib.Path().absolute())+"/Fichero_texto2.txt","a")


archivo.write("********SOY UN TEXTO METIDO DESDE PYTHON********\n")

archivo.close()


#Abrir un archivo
archivo_lectura = open(str(pathlib.Path().absolute())+"/Fichero_texto2.txt","r")

#Leer Contenido
contendo = archivo_lectura.read()
print(contendo)


lista = archivo_lectura.readline()

archivo_lectura.close

print(lista)

"""
#copiar
ruta = str(pathlib.Path().absolute())+ "/Fichero_texto2.txt"
ruta_new = str(pathlib.Path().absolute())+ "/f1copy.txt"
shutil.copyfile(ruta,ruta_new)
"""
#Mover
"""
ruta = str(pathlib.Path().absolute())+ "/F1.txt"
ruta_new = str(pathlib.Path().absolute())+ "/Hola.txt"

shutil.move(ruta,ruta_new)

"""

"""
ruta_new = str(pathlib.Path().absolute())+ "/Hola.txt"
os.remove(ruta_new)
"""
ruta_comprobar = str(pathlib.Path().absolute())+ "/F1copy.txt"

if os.path.isfile(ruta_comprobar):
    print("El Archivo Existe")
else:
    print("El Archivo no existe")

