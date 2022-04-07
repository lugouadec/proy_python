import os

#Crear una carpeta
if not os.path.isdir("./Mi_carpeta"):
    os.mkdir("./Mi_carpeta")
else:
    print("Ya existe el directorio")
    
# Eliminar una Carpeta
#os.rmdir("./Mi_carpeta")

# Copiar una Carpert shutill.copytree(ruta_origen, ruta_destino)

print("contenido de mi carpeta")

contenido = os.listdir("./Mi_carpeta")

for fichero in contenido:
    print(fichero)

