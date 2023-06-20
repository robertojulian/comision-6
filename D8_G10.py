import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
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

    def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            self.online = True
            print("Inicio de sesión exitoso")
        else:
            print("Nombre de usuario o contraseña incorrectos")

    def registrar(self):
        print("Registrando usuario...")
        # Lógica para registrar al usuario en la base de datos o en algún sistema de almacenamiento
        self.fecha_registro = datetime.datetime.now()
        print("Usuario registrado exitosamente")

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico

    def comentar(self, comentario):
        if self.online:
            print("Comentario:", comentario)
        else:
            print("Debes iniciar sesión para poder comentar.")

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador

    def publicar(self, contenido):
        if self.online:
            print("Publicación realizada:", contenido)
        else:
            print("Debes iniciar sesión para poder publicar.")

usuarios_registrados = []

while True:
    print("Bienvenido al programa de Registro e Inicio de Sesión")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Comentar como público")
    print("4. Publicar como colaborador")
    print("5. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        id = len(usuarios_registrados) + 1
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su teléfono: ")
        username = input("Ingrese su nombre de usuario: ")
        email = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese su contraseña: ")
        avatar = input("Ingrese el nombre de su avatar: ")

        nuevo_usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, None, avatar, "Activo", False)
        nuevo_usuario.registrar()
        usuarios_registrados.append(nuevo_usuario)

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
        else:
            print("Usuario no encontrado. Debes registrarte primero.")

    elif opcion == "3":
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        usuario_encontrado = None
        for usuario in usuarios_registrados:
            if isinstance(usuario, Publico) and usuario.username == username:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            usuario_encontrado.login(username, contraseña)
            usuario_encontrado.comentar()
        else:
            print("Usuario público no encontrado. Debes registrarte como público primero.")

    elif opcion == "4":
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        usuario_encontrado = None
        for usuario in usuarios_registrados:
            if isinstance(usuario, Colaborador) and usuario.username == username:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            usuario_encontrado.login(username, contraseña)
            usuario_encontrado.publicar()
        else:
            print("Usuario colaborador no encontrado. Debes registrarte como colaborador primero.")

    elif opcion == "5":
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")