import sqlite3

#Conexion 
conexion = sqlite3.connect('pruebas.db')

#crear cursor
cursor = conexion.cursor()


# Crear Una Tabla

cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
                titulo varchar(255),
                descripcion text,
                precio int(255))
               ''')

#Guardar Cambios 
conexion.commit()

#Insertar Datos
#cursor.execute('''INSERT INTO productos VALUES (null,'Primer producto','Descripcion de mi producto',550)''')
#conexion.commit()

#Actualizar 
cursor.execute("update productos set precio = 668 where id = 1")
conexion.commit()

#Listar datos
cursor.execute('''SELECT * FROM productos;''')
productos = cursor.fetchall()

for producto in productos:
    print("--------------------------------------------------------")
    print(f"Numero: {producto[0]} \nNombre: {producto[1]}\nProducto: {producto[2]}\nPrecio: {producto[3]}\n\n")

print(productos)


#Cerrar la conexion
conexion.close()
