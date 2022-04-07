import usuarios.usuario as modelo

class Acciones:
    
    def registro(self):
        print("Ok !! Vamos a registrar en el sistemas...")
        nombre = input("¿Cual es tu nobre?") 
        apellidos = input("¿Cual es tu apelldos?")
        email = input("¿Cual es tu email?")
        password = input("¿Cual es tu passwod?")
        
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro =  usuario.registrar()
        
        if registro[0] >= 1 :
            print(f"Perfecto {registro[1].nombre}, te has registrado con el mail {registro[1].email}")
        else:
            print ("No te has registrado correctamente !!!")
        
    def login(self):
        print ("Vale !! Identificate en el sistemas")
        email = input("¿Cual es tu email?")
        password = input("¿Cual es tu passwod?")
        

