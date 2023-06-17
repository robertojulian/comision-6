class Blog():
    def __init__(self):
        self.lista_usuarios = []
        self.lista_comentarios =[]
        self.lista_articulos =[]

    def agregar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)

    def agregar_comentario(self, comentario):
        self.lista_comentarios.append(comentario)

    def agregar_articulo(self, articulo):
        self.lista_articulos.append(articulo)

    def mostrar_lista(self)

class Usuario():
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasenia = contrasenia
        self.fecha_de_registro = fecha_de_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def login(self, us, passw):
        while True:
            if us == self.username:
                if passw == self.contrasenia:
                      return(f"bienvenido {self.nombre}")
                      break
                else:
                    return("\nUsuario y/o contraseña incorrecta. Intente nuevamente.\n")
            else:
                  return("\n Usuario  inválido. Intente nuevamente.\n")
            """pruebo con un usuario inventado y  funciona: 
x = Usuario(0, 0, 0, 0, "ana_maria", 0, 1234, 0, 0, 0, 0)
print(x.login("ana_maria", 1234))
   
"""  
    def registrar(self):
            for i in Usuario.id:
                i.id+=1
            Blog.agregar_usuario()

 
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
        self.es_publico=es_publico

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenia, fecha_de_registro, avatar, estado, online)
        self.es_colaborador=es_colaborador
         



#Código para elegir entre registrar usuarios o hacer login (si ya está registrado).

while True:
    comando = input("Ingrese una orden:\n1-Regsitrarse \n2-Login \n3-Salir \nRespuesta: ")

    if comando == "1":
       
        aid=
        anombre = input("\ningrese su nombre:")
        aapellido = input("\ningrese su apellido:")
        atelefono = input("\ningrese su telefono:")
        ausername = input("\ningrese su nombre de usuario:")
        aemail = input("\ningrese su email:")
        acontrasenia = input("\ningrese su contraseña:")
        afecha_de_registro = input("\ningrese su fecha_de_registro:")
        aavatar = input("\ningrese su avatar:")
        aestado = input("\ningrese su estado:")
        aonline = input("\nesta online?:")

        Usuario.registrar(aid,anombre,)
        Blog.agregar_usuario
        


    elif comando == "2":
        Usuario.login()

    elif comando == "3":
        break # Salir del bucle principal y finalizar el programa

    else:
        print("Orden no reconocida. Intente nuevamente.")