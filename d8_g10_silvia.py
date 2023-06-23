import datetime
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar=None, estado=True, online=False):
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

    def __str__(self):
        if self.online:
            conectado = "conectado"
        else:
            conectado = "Desconectado"
        return f"El usuario es {self.usuario} y está {conectado}"
        
    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Inicio de sesión exitoso")
            
        else:
            print("Nombre de usuario o contraseña incorrectos")
    
    def comentar(self, comentario):
        if self.online:
            print("Comentario:", comentario)##comentar con rol de colaborador o publico
        else:
            print("Debes iniciar sesión para poder comentar.")

    def registrar(self):
        print("Registrando usuario...")
        # Lógica para registrar al usuario en la base de datos o en algún sistema de almacenamiento
        self.fecha_registro = datetime.datetime.now()
        print("Usuario registrado exitosamente")
    
    def mostrar(self):
        print("Usuario:", self.username)
        print("Contraseña: ",self.contraseña)

#subclase Publico
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico

#subclase Colaborador        
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador

    def publicar(self, contenido):
        if self.online:
            print("Publicación realizada:", contenido)#publicar el articulo
        else:
            print("Debes iniciar sesión para poder publicar.")

#constructor
class Articulo:
    def __init__(self,id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = datetime.now()
        self.imagen = imagen
        self.estado = True
    
    def __str__(self):
        return Articulo.__str__(self) + ", Titulo: {} , Resumen {}".format(self.username, self.resumen)

#constructor
class Comentario:
    def __init__(self,id,id_articulo, id_usuario,contenido,fecha_hora,estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = True

    
usuarios_registrados = [] #lista para usuarios registrados
lista_articulos = [] #lista de articulos
lista_comentarios = [] #lista de comentarios

def alta_comentario(id_a,cant_c,id_u):
    #self,id,id_articulo, id_usuario,contenido,fecha_hora,estado
    id = cant_c
    id_articulo = id_a
    id_usuario = id_u
    contenido = input("Contenido: ")
    fecha_comentario = datetime.now
    estado = True
    comentario_nuevo = Comentario(id, id_articulo, id_usuario, contenido, fecha_comentario, estado)

def mostrar_todos_comentarios_arts():
    print("Lista de Articulos")
    for a1 in range(len(lista_articulos)):
        print(a1+1,"-",lista_articulos[a1])
        for c1 in range(len(lista_comentarios)):
            print("--> ",c1+1, " -", lista_comentarios[c1],"\n")
  
def operaciones_publico(usuario):
    while True:
        mostrar_todos_comentarios_arts()#mostrar la lista de articuls con sus comentarios para seleccionar el articulo
        print("1. Comentar un artículo existente")
        print("2. Cancelar")
        opcion_c = int(input("Ingrese su opcion: "))
        if opcion_c == 1:
            indice_articulo = int(input("Seleccionar el indice del articulo a comentar  entre 1 y ", len(lista_articulos)))
            if indice_articulo >= 0 and indice_articulo <= len(lista_articulos):
                #comentar articulo
                alta_comentario(indice_articulo, len(lista_comentarios), usuario.id)
                mostrar_todos_comentarios_arts()
            else:
                print("No se selecciono un indice valido")
        else:
            print("Operación cancelada")
        
def operaciones_colaborador(usuario):
    while True:
        mostrar_todos_comentarios_arts()
        print("1. Publicar un nuevo artículo")
        print("2. Comentar un artículo existente")
        print("3. Cancelar")
        opcion_c = int(input("ingrese su opcion: "))
        
        if opcion_c == 1:
            print("Alta del articulo. ") #id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
            id_articulo = len(lista_articulos)+1
            id_usuario = usuario.id 
            titulo = input("Titulo: ")
            resumen = input("Resumen: ")
            contenido = input("Contenido: ")
            fecha_articulo = datetime.now()
            imagen = None
            estado = True
            articulo_nuevo =Articulo(id_articulo, id_usuario, titulo, resumen, contenido, fecha_articulo,imagen,estado)
            lista_articulos.append(articulo_nuevo)
            mostrar_todos_comentarios_arts()
        elif opcion_c == 2: #comentar el articulo
            indice_articulo = int(input("Seleccionar el indice del articulo a comentar  entre 1 y ", len(lista_articulos)))
            if indice_articulo >= 0 and indice_articulo <= len(lista_articulos):
                #comentar articulo
                alta_comentario(indice_articulo, len(lista_comentarios), usuario.id)
                mostrar_todos_comentarios_arts()
            else:
                print("No se selecciono un indice valido")
        else:
            print("Operación cancelada")

def menu_principal():
    while True:
        print("Bienvenido al programa de Registro e Inicio de Sesión")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        opcion = input("Ingrese su opción - 3. para Salir: ")

        if opcion == "1":
            id = len(usuarios_registrados) + 1
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = input("Ingrese su teléfono: ")
            username = input("Ingrese su nombre de usuario: ")
            email = input("Ingrese su correo electrónico: ")
            contraseña = input("Ingrese su contraseña: ")
            avatar = input("Ingrese el nombre de su avatar: ")
            tipo_usuario = int(input("Ingrese el tipo de usuario 1-Colaborador 2-Publico: "))
            if tipo_usuario == 1:
                nuevo_usuario = Colaborador(id, nombre, apellido, telefono, username, email, contraseña, None, avatar, True, False,True)
            else:
                nuevo_usuario = Publico(id, nombre, apellido, telefono, username, email, contraseña, None, avatar, True, False,True)
            nuevo_usuario.registrar()
            usuarios_registrados.append(nuevo_usuario)
            nuevo_usuario.mostrar()
      
        elif opcion == "2":
            username = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            usuario_encontrado = None
            for usuario in usuarios_registrados:
                if usuario.username == username:
                    usuario_encontrado = usuario
                    break
            if usuario_encontrado:
                usuario_encontrado.login(username, contraseña)
                if isinstance(usuario_encontrado,Colaborador):
                    operaciones_colaborador(usuario_encontrado) #funcion para publicar o comentar como colaborador
                else:
                    operaciones_publico(usuario_encontrado) #funcion para comentar como publico
            else:
                print("Usuario no encontrado. Debes registrarte primero.")

        elif opcion == "3":
            print("Fin del proceso")
            break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

menu_principal()
