# Instalar el connector de Mysql #: pip install mysql-connector-python

import mysql.connector

#Conexion a la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="master_python"
)

#¿Como se que la conexion es correcta
#print (database)

#Crear la Base de Datos

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db[0])
    
    
print("-----------------crear tablas-------------------")
#Crear tablas
cursor.execute('''
               CREATE TABLE IF NOT EXISTS vehiculos(
                   id int(10) auto_increment not null,
                   marca varchar(40) not null,
                   modelo varchar(40) not null,
                   precio float(10,2) not null,
                   CONSTRAINT pk_vehiculo PRIMARY KEY(id)
               ) 
               ''')

cursor.execute("desc vehiculos")


for db in cursor:
    print(db[0])


#Insertar Datos    
#cursor.execute("insert into vehiculos values(null,'Opel','Astra',180500)")
#database.commit()

#Insertar Datos Macivos
coches = [
    ('Seat','Ibiza', 50000),
    ('Nissan','Sentra', 505000),
    ('Ford','Lobo', 1225000),  
    ('Mercedes','Clase C', 35000),  
]

#cursor.executemany("insert into vehiculos Values(null,%s,%s,%s)",coches)
#database.commit()

cursor.execute("Select * from vehiculos")

result = cursor.fetchall() ##fetchone solo saca un renglon de la consulta 

for db in result :
    print("-------------------------------")
    print (db[0])
    print (db[1])
    print (db[2])
    print (str(db[3])+"\n")


#Borrar un dato    
cursor.execute("delete from vehiculos where id = 1")
database.commit()

print(cursor.rowcount,"Borrados!!!")

#Actualizar Datos
cursor.execute("update vehiculos set modelo='Leon' where modelo='Ibiza'")

database.commit()
print(cursor.rowcount,"Acutalizados")



