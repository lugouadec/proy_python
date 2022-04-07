"""
    Proyecto Python y Mysql
    -Abri asistente
    - Login o registro
    - Si elegimos registro, creara un usuario en la BBDD
    - Si elegimos login, identifica al usuario y nos preguntara 
    - crear nota, mostrar notas, borrarlas.
"""

from usuarios import acciones

print ('''
Acciones disponibles:
    - registro
    - login
    ''')

hazEL = acciones.Acciones()

print(type(hazEL))


accion = input("¿Que quieres hacer: ")

if accion == "registro":
    hazEL.registro()
    
elif accion == "login":
    hazEL.login()
    
    