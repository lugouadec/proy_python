import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "",
    database = "master_python",
  #  port = "3306"
)

cursor = database.cursor(buffered=True)


class Usuario:
    
    def __init__(self,nombre, apellios, email, password):
        self.nombre = nombre
        self.apellidos = apellios
        self.email = email
        self.password = password
        
    def registrar(self) :
        #fecha = "2022-01-01"
        #fecha = datetime.datetime.now().strftime('%Y-%m-%d')
        fecha = datetime.datetime.now()
        print("--------------------------------")
        print(type(fecha))
        print (fecha)
        print("--------------------------------")
        
        sql = "insert into usuarios values(null,%s,%s,%s,%s,%s)"
        #print(sql)
        usuario = (self.nombre,self.apellidos,self.email,self.password,fecha)
        #print (usuario)
        cursor.execute(sql,usuario)
        database.commit()
        
        return [cursor.rowcount, self]
    
    def identificar(self):
        return self.nombre