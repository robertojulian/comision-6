import datetime
class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, avatar):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.fecha_registro = None
        self.avatar = avatar
        self.estado = None
        self.online = None
    def __str__(self):
        return f'id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Telefono: {self.telefono}, ' \
               f'Username: {self.username}, Email: {self.email}, Contraseña: {self.contrasena}, ' \
               f'Fecha de registro: {self.fecha_registro}, Avatar: {self.avatar}, Estado: {self.estado}, ' \
               f'Online: {self.online}'
    def set_login(self):        
        if self.online == False:
            self.online = True
            print('Inicio de sesión exitoso!!!')
        else:
            self.online= False
            print('Sesión Finalizada. Adios')
    def set_registrar(self):
        self.fecha_registro = datetime.date.today()
        self.estado = True
        self.online = False
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena,avatar):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena,avatar)
        self.es_publico = None
    def __str__(self):
        return super().__str__() + f' Es_publico: {self.es_publico}'
    def set_registrar(self):
        super().set_registrar()
        self.es_publico= True 
    def set_login(self):
        return super().set_login()
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena,avatar):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasena,avatar)
        self.es_colaborador = None
    def __str__(self):
        return super().__str__() + f' Es_colaborador: {self.es_colaborador}'
    def set_registrar(self):
        super().set_registrar()
        self.es_colaborador = True
    def set_login(self):
        return super().set_login()
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, imagen):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = None
        self.imagen = imagen
        self.estado = None
    def __str__(self):
        return f' {self.id} - Título: {self.titulo},\n Resumen: {self.resumen},\n ' \
               f'Contenido: {self.contenido},\n Fecha Publicación: {self.fecha_publicacion},\n Imagen: {self.imagen}'
    def set_publicar_articulo(self):
        self.fecha_publicacion = datetime.date.today().strftime('%d-%m-%y')
        self.estado = True
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = None
        self.estado = None
    def __str__(self):
        return f'Comentario: {self.contenido}, Fecha/hora: {self.fecha_hora}'
    def set_comentario(self):
        self.fecha_hora = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.estado = True
    def set_id(self,lista):
        if len(lista)==0:
            self.id = 1        
        else:
            self.id = lista[-1].id + 1  
        return id
def mostrar_articulos():
    if len(lista_articulos) ==0:
        print('------------------')
        print('No existe ningún artículo para mostrar.')
        print('------------------')
    else:
        print('------ARTICULOS------')
        for articulo in lista_articulos:
            print(articulo)
            print('------------------')
def mostrar_articulo_comentarios(id_articulo):
    print('------------------')
    for articulo in lista_articulos:
        if articulo.id == id_articulo:
            print('------------------')
            print('________ARTICULO________')
            print(articulo)
            print('------------------')
            print('COMENTARIOS:')
            for comentario in lista_comentarios:
                if comentario.id_articulo == id_articulo:
                    for usuario in lista_usuarios:
                        if usuario.id == comentario.id_usuario:
                            print(f'        Usuario: {usuario.username} {comentario}.')
def mostrar_todos_articulos_comentarios():
    for articulo in lista_articulos:
        print('------------------')
        print('________ARTICULO________')
        print(articulo)
        print('------------------')
        print('COMENTARIOS:')
        for comentario in lista_comentarios:
            if comentario.id_articulo == articulo.id:
                for usuario in lista_usuarios:
                    if usuario.id == comentario.id_usuario:
                        print(f'        Usuario: {usuario.username} {comentario}.')
def existe_usuario(username):
    for usuario in lista_usuarios:
        if usuario.username == username:
            return True
    return False
def ingresar_validar(texto):
    while True:
        dato = input(texto)
        if texto=='Teléfono: 'and dato.isdigit() == False:
            print('En teléfono solo puede ingresar numeros.-')
        elif texto=='Contraseña: ' and len(dato)<6:
            print('La contraseña debe contener mínimo 6 digitos.-')
        elif dato.upper() == 'EXIT' or dato != '':        
            return dato        
def buscar_articulo(id_articulo_elegido):
    for articulo in lista_articulos:
        if articulo.id == id_articulo_elegido:
            return articulo
def crear_id(texto):
    if texto=='usuario':
        if len(lista_usuarios)==0:
            id=1
        else:
            id = lista_usuarios[-1].id+1
    elif texto=='articulo':
        if len(lista_articulos)==0:
            id=1
        else:
            id = lista_articulos[-1].id+1
    else:
        if len(lista_comentarios)==0:
            id=1
        else:
            id = lista_comentarios[-1].id+1
    return id
def usuario_logueado():
    for usuario in lista_usuarios:
        if usuario.online == True:
            return usuario
def menu_usuario_publico():
    while True:
        try:
            op = int(input("Elige una opción: \n1. Comentar un articulo. \n2. Listar articulos y comentarios. \n3. Cerrar sesión.  \nIngrese ópcion: "))
            if op==1:
                print('------------------')
                mostrar_articulos()
                print('------------------')
                if len(lista_articulos)!=0:
                    while True:
                        id_articulo_elegido = int(input('Ingrese el nro del artículo que quiere comentar: '))
                        contenido = ingresar_validar('Ingrese comentario: ')
                        if buscar_articulo(id_articulo_elegido):
                            nuevo_comentario= Comentario(crear_id('comentario'),id_articulo_elegido,usuario_logueado.id,contenido)
                            nuevo_comentario.set_comentario()
                            lista_comentarios.append(nuevo_comentario)
                            print('Comentario agregado con éxito.-')
                            print('------------------')
                            mostrar_articulo_comentarios(id_articulo_elegido)
                            break
                        else:
                            print('Opción inválida. Inténtalo nuevamente.')
                            print('------------------')
            elif op == 2:
                print('------------------')
                mostrar_todos_articulos_comentarios()
                print('------------------')
            elif op == 3:
                print('------------------')
                usuario_logueado().set_login()
                break
        except ValueError:
            print('------------------')
            print("Opción inválida. Inténtalo nuevamente.")
            print('------------------')
def menu_usuario_colaborador():
    while True:  
        try:                          
            op = int(input("Elige una opción: \n1. Comentar un artículo. \n2. Publicar Artículo. \n3. Listar Articulos y Comentarios.  \n4. Cerrar sesión. \nIngrese ópcion: "))
            if op==1:
                mostrar_articulos()
                if len(lista_articulos) !=0:
                    while True:
                        id_articulo_elegido = int(input('Ingrese el nro del articulo que quiere comentar: '))
                        if buscar_articulo(id_articulo_elegido):
                            contenido = ingresar_validar('Ingrese comentario: ')
                            nuevo_comentario= Comentario(crear_id('comentario'),id_articulo_elegido,usuario_logueado().id,contenido)
                            nuevo_comentario.set_comentario()
                            lista_comentarios.append(nuevo_comentario)
                            print('------------------')
                            print('Comentario agregado con éxito.-')
                            print('------------------')
                            mostrar_articulo_comentarios(id_articulo_elegido)
                            break
                        else:
                            print('------------------')
                            print('Opción inválida. Inténtalo nuevamente.')
                            print('------------------')
            elif op ==2:
                print('------------------')
                titulo = ingresar_validar('Título: ')
                resumen = ingresar_validar('Resumen: ')
                contenido = ingresar_validar('Contenido: ')
                imagen = 'Imagen'
                nuevo_articulo= Articulo(crear_id('articulo'),usuario_logueado().id,titulo,resumen,contenido,imagen)
                nuevo_articulo.set_publicar_articulo()
                lista_articulos.append(nuevo_articulo)
                print('------------------')
                print('Articulo agregado con éxito.-')
                print('------------------')
            elif op ==3:
                mostrar_todos_articulos_comentarios()
            elif op == 4:
                print('------------------')
                usuario_logueado().set_login()
                print('------------------')
                break
        except ValueError:
            print('------------------')
            print("Opción inválida. Inténtalo nuevamente.")
            print('------------------')
def menu_principal():
    while True:
        try:        
            op = int(input("Elige una opción: \n1. Registrarse \n2. Loguearse \n3. Salir \nIngrese opción: "))
            if op == 1:
                print('')
                while True:
                    try:
                        print('------------------')                   
                        op = int(input("Elige el tipo de usuario: \n1. Usuario Público \n2. Colaborador \n3. Volver al Menu Anterior \nIngrese opción: "))
                        if op == 1:
                            while True:
                                print('')
                                print('------ [ Escriba EXIT para cancelar y salir ] ------')
                                print('---------- INGRESE LOS DATOS DEL USUARIO --------')
                                nombre = ingresar_validar('Nombre: ')
                                if nombre.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                apellido = ingresar_validar('Apellido: ')
                                if apellido.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                telefono = ingresar_validar('Teléfono: ')
                                if telefono.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                username = ingresar_validar('Username: ')
                                if username.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                email = ingresar_validar('Email: ')
                                if email.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                contrasena = ingresar_validar('Contraseña: ')
                                if contrasena.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                print('')
                                print('------            DATOS INGRESADOS            ------')
                                print(f'Nombre: {nombre} \nApellido: {apellido} \nTeléfono: {telefono} \nUsername: {username} \nEmail: {email} \nContraseña: {contrasena}')
                                print('------------------')
                                print('Confirma = 1     Volver a ingresar datos = 2     Volver menú anterior = 3')
                                respuesta = input('Ingrese opción: ')
                                try:
                                    if respuesta == '1' and respuesta == '3':
                                        break
                                except ValueError:
                                    print("Opción inválida. Inténtalo nuevamente.")
                                if respuesta=='1':
                                    avatar = 'imagen'
                                    if existe_usuario(username)== True:
                                        print('El username ingresado ya está en uso.')  
                                        print('------------------')
                                        break
                                    print('------------------')
                                    usuario_nuevo= Publico(crear_id('usuario'),nombre,apellido,telefono,username,email,contrasena,avatar)    
                                    usuario_nuevo.set_registrar()
                                    lista_usuarios.append(usuario_nuevo)
                                    print ('Usuario Público registrado con éxito')
                                    print('')
                                    break
                                if respuesta=='3':
                                    break  
                            if respuesta=='1':
                                    break 
                        elif op == 2:
                            while True:
                                print('')
                                print('------ [ Escriba EXIT para cancelar y salir ] ------')
                                print('------     INGRESE LOS DATOS DEL USUARIO      ------')
                                nombre = ingresar_validar('Nombre: ')
                                if nombre.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                apellido = ingresar_validar('Apellido: ')
                                if apellido.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                telefono = ingresar_validar('Teléfono: ')
                                if telefono.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                username = ingresar_validar('Username: ')
                                if username.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                email = ingresar_validar('Email: ')
                                if email.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                contrasena = ingresar_validar('Contraseña: ')
                                if contrasena.upper() == 'EXIT':
                                    respuesta='3'
                                    break
                                print('')
                                print('------ DATOS INGRESADOS ------')
                                print(f'Nombre: {nombre} \nApellido: {apellido} \nTeléfono: {telefono} \nUsername: {username} \nEmail: {email} \nContraseña: {contrasena}')
                                print('------------------')
                                print('Confirma = 1     Volver a ingresar datos = 2     Volver menú anterior = 3')
                                respuesta = input('Ingrese opción: ')
                                try:
                                    if respuesta == '1' and respuesta == '3':
                                        break
                                except ValueError:
                                    print("Opción inválida. Inténtalo nuevamente.")
                                if respuesta=='1':
                                    avatar = 'imagen'
                                    if existe_usuario(username)== True:
                                        print('El username ingresado ya está en uso.')  
                                        print('------------------')
                                        break
                                    print('------------------')
                                    usuario_nuevo= Colaborador(crear_id('usuario'),nombre,apellido,telefono,username,email,contrasena,avatar)    
                                    usuario_nuevo.set_registrar()
                                    lista_usuarios.append(usuario_nuevo)
                                    print ('Usuario Colaborador registrado con éxito')
                                    print('')
                                    break
                                if respuesta=='3':
                                    break  
                            if respuesta=='1':
                                break                                         
                        elif op == 3:
                            print('------------------')
                            break
                    except ValueError:
                        print("Opción inválida. Inténtalo nuevamente.")                
            elif op == 2:
                if len(lista_usuarios)!=0:
                    print('------LOGIN------')
                    username = ingresar_validar("Username: ")
                    if existe_usuario(username):
                        contrasena = ingresar_validar("Contraseña: ")
                        for usuario in lista_usuarios:
                            if usuario.username == username and usuario.contrasena == contrasena:
                                usuario.set_login()
                                print('------------------')
                                print(f'Usuario: {usuario.username}, Apellido: {usuario.apellido}, Nombre: {usuario.nombre}, Tipo: {usuario.__class__.__name__}')
                                print('------------------')
                                if isinstance(usuario,Publico):
                                    menu_usuario_publico()
                                else:
                                    menu_usuario_colaborador()             
                                break
                            else:
                                print("Inicio de sesión fallido. Verifica tus credenciales.")
                                print('------------------')
                    else:
                        print('------------------')
                        print('Usuario incorrecto, vuelva a intentarlo.-')
                        print('------------------')
                else:
                    print('------------------')
                    print('No existe ningun usuario, debe registrarse!!!')
                    print('------------------')
                    print('')
            elif op == 3:
                print('')
                print('--------- FIN ---------')
                break        
        except ValueError:
            print('------------------')
            print("Opción inválida. Inténtalo nuevamente.")
            print('------------------')

# PROGRAMA
lista_usuarios = []
lista_articulos = []
lista_comentarios = []
print('------BIENVENIDO------')
menu_principal()