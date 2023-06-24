#importar para saber fecha de creacion del usuario
import datetime

#crear una lista donde el metodo registrar guarde los nuevos usuarios creados      
class ListaUsuarios():
    def __init__(self):
        self.lista_usuarios = []

    #metodo para agregar usuarios a lista_usuarios
    def registrar(self, usuarios):
        if not isinstance(usuarios, Usuario):
            print("Tipo de dato no permitido")
            return
        for u in self.lista_usuarios:
            if u.id == usuarios.id:
                print("Id existente")
                return
        self.lista_usuarios.append(usuarios)

    #metodo para ver lista_usuarios       
    def ver_info1(self):
        for u in self.lista_usuarios:
            print("ID: %s" % (u.id))
            print("Nombre: %s" % (u.nombre))
            print("user: %s" % (u.username))
            print("contra: %s" % (u.contraseña))    
            print("ghola: %s" % (u.telefono)) 
            print("ghola: %s" % (u.fecha_registro))




#Clase usuario
class Usuario:
  
    def __init__(self, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
        
    #metodo para logearse
    def login(self,username,contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Ingreso correctamente")
        elif self.username != username or self.contraseña != contraseña: 
            print("Intente nuevamente")
       
    def ver_info(self):
        print("ID: %s" % (self.id))
        print("Nombre: %s" % (self.nombre))
        print("user: %s" % (self.username))
        print("contra: %s" % (self.contraseña))
        
    
class Publico(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online,es_publico):
        super().__init__(nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico

    def registrar(self):
        es_publico = True
        es_publico.registrar()

    def comentar(self,comentario):
        comentario = input("Agregar un comentario: ")
        print(comentario)


class Colaborador(Usuario):
    def __init__(self, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online,es_colaborador):
        super().__init__(nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador

    def registrar(self):
        return
    
    def comentar(self):
        return
    
    def publicar(self):
        return

class Articulo():
    def __init__(self,id, id_usuario,resumen,contenido,fecha_publicacion,imagen,estado):
        self.id = id 
        self.id_usuario = id_usuario
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado


class Comentario():
    def __init__(self,id,id_articulo,id_usuario,contenido,fecha_hora,estado):
        self.id = id
        self.id_articulo = Articulo(id_articulo)
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado





#asignar una variable a la lista_usuarios
l_u = ListaUsuarios()

def verificar_bool():
    if avatar == "s" or estado == "s" or online == "s":
        print(" True")
    elif avatar == "n" or estado == "n" or online == "n":
        print("False")
    else:
        ("Valor ingresado no valido")
#menu 
while True:
    print("\n--- Menú ---")
    print("1. Agregar usuario")
    print("2. Ingresar usuario")
    print("3. Calcular precio total de una marca de bebida")
    print("4. Eliminar un producto")
    print("5. Mostrar información")
    print("0. Salir")

    opcion = int(input("Ingrese el número de la opción que desea ejecutar: "))

    if opcion == 1:
        id = id
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = int(input("Ingresar número de teléfono: "))
        username = input("Ingrese un nombre de usuario: ")
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese una contraseña: ")
        fecha_registro = datetime.datetime.now()
        avatar= input("Tiene avatar?\nS o N: ").lower()
        verificar_bool()
        estado = input("S o N: ")
        verificar_bool()
        online = input("Esta en linea?\nS o N: ")
        verificar_bool()
        usuarios = Usuario(nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        l_u.registrar(usuarios)

    elif opcion == 2:
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        usuarios.login(username,contraseña)
        
        
        


      
    # elif opcion == 3:

    # elif opcion == 4:

    elif opcion == 5:
        ListaUsuarios.ver_info1(l_u)

    elif opcion == 0:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")



