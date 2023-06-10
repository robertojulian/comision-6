-- Desafío 7: Scripts de SQL – Blog
/*Integrantes Grupo 10:
Chavez Roberto
Diaz Juan Pablo
Ferreyra Fernando
Kliokis Federico
Leguizamon Rafael Marcelo
Lucas Jorge
Llanes Silvia
Portillo Valentina
Ramirez Nelida
Zalazar Bruno*/

-- Creacion de la base de datos
CREATE DATABASE blog;
USE blog;
-- Creacion de la tabla usuario
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(50) NOT NULL,
    fecha_creacion DATE NOT NULL,
    avatar BLOB NULL,
    estado BOOLEAN NOT NULL,
    es_publico BOOLEAN NOT NULL,
    es_colaborador BOOLEAN NOT NULL,
    es_admin BOOLEAN NOT NULL
   );
-- Creacion de la tabla articulo
CREATE TABLE articulo (
	id_articulo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    resumen VARCHAR(100) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE NOT NULL,
    estado BOOLEAN NOT NULL,
    imagen BLOB NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id)
    );

-- Creacion de la tabla comentario
CREATE TABLE comentario (
	id_comentario INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    contenido TEXT,
    fecha_hora DATETIME,
    estado BOOLEAN NOT NULL,
    id_articulo INT NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY(id_articulo) REFERENCES articulo(id_articulo),
    FOREIGN KEY(id_usuario) REFERENCES usuario(id)
    );
 
 -- Creacion de la tabla categoria
CREATE TABLE categoria (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    imagen BLOB,
    estado BOOLEAN NOT NULL,
    id_categoria INT,
    FOREIGN KEY(id_categoria) REFERENCES categoria(id)
   );
   -- Creacion de la tabla categoria_articulo
   CREATE TABLE categoria_articulo (
	id_categoria_articulo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_articulo INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY(id_articulo) REFERENCES articulo(id_articulo),
    FOREIGN KEY(id_categoria) REFERENCES categoria(id)
    );
    
/*1) Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol
de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos:
es_publico, es_colaborador y es_admin son booleanos.*/
 INSERT INTO usuario VALUES (1, 'Juan', 'Sánchez', '3624202020', 'juanperez@gmail.com', 'juanperez', '2022-01-01',NULL, True, False, False,True), 
							(2, 'Maria', 'Gomez', '3624202626', 'colab1@gmail.com', 'colab1', '2022-01-02',NULL,True, False, True,False),
							(3, 'Pedro', 'Perez', '3624203333', 'colab2@gmail.com', 'colab2', '2022-01-03',NULL,True, False, True,False),
							(4, 'Luis', 'Villa', '3624206666', 'colab3@gmail.com', 'colab3', '2022-01-04',NULL,True, False, True,False),
							(5, 'Teresa', 'Romero', '3624207777', 'colab4@gmail.com', 'colab4', '2022-01-05',NULL,True, False, True,False),
							(6, 'Esteban', 'Esquivel', '3624201111', 'PUBLICO1@gmail.com', 'PUBLICO1', '2022-01-02', NULL, True, TRUE, FALSE,FALSE),
							(7, 'Pedro', 'Tetaz', '3624209999', 'PUBLICO2@gmail.com', 'PUBLICO2', '2022-01-03',NULL, True, TRUE, FALSE,FALSE),
							(8, 'Eusebio', 'Almaraz', '3624200505', 'PUBLICO3@gmail.com', 'PUBLICO3', '2022-01-04',NULL, True, TRUE, FALSE,FALSE),
							(9, 'Aitana', 'Remez', '3624200303', 'PUBLICO4@gmail.com', 'PUBLICO4', '2022-01-05',NULL, True, TRUE, FALSE,FALSE),
							(10, 'Vladimir', 'Mierez', '3624204242', 'PUBLICO5@gmail.com', 'PUBLICO5', '2022-01-05',NULL, True, TRUE, FALSE,FALSE);
-- SELECT * FROM USUARIO;
 
 /*2) Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios agregado con rol de colaborador*/
 UPDATE usuario
 SET es_colaborador = FALSE,es_admin = TRUE
 WHERE id = 2 AND es_colaborador = TRUE;
-- SELECT * FROM USUARIO;
/*3) Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
Booleano */
INSERT INTO articulo VALUES (1, 'Día Mundial del Medio Ambiente', 'Desarrollo sustentable y en la protección del medio ambiente.', 'La protección del medio ambiente requiere de esfuerzos colaborativos', '2023-02-01', TRUE,NULL, 3),
							(2, 'Concientizar sobre el cuidado del Medioambiente', 'La concientización y el conocimiento de nuestra biodiversidad', 'Para todos aquellos que deseen participar', '2023-02-05',TRUE, NULL, 3),
							(3, 'El uso racional de la energía', 'El diagnóstico sobre la cuestión ambiental', 'La empresa está obligada a asumir la responsabilidad que le compete por el mal uso de los recursos no renovables', '2023-02-02', TRUE, NULL, 4),
							(4, '10 acciones que impulsa Chile en medio ambiente', 'Apostar por la generación de energía limpia', 'El Senado chileno aprobó la integración del país al Acuerdo de Escazú', '2023-02-05', FALSE, NULL, 4); 

-- SELECT * FROM ARTICULO;

/*4) Agregar el comando necesario para eliminar el artículo que tenga estado FALSE */
DELETE FROM articulo WHERE estado = false;

/* 5) Agregar el comando necesario que introduzca 3 comentarios al primer artículo agregado y 2 comentarios al segundo artículo*/
INSERT INTO comentario VALUES (1,'Cada año, la humanidad produce 400 millones de toneladas de plásticos','2023-02-20 05:05:16', TRUE,1,6),
								(2,'Los microplásticos que contaminan aire y agua, representan una amenaza para la salud humana y la del planeta','2023-02-21 05:06:00', TRUE,1,7),
								(3,'No solo se trata de proteger la naturaleza, sino también de proteger la propia supervivencia humana','2023-02-20 05:07:16', TRUE,1,8),
								(4,'Talleres Río Grande en Invierno','2023-02-20 05:15:17', TRUE,2,6),
								(5,'Propuestas para toda la comunidad.','2023-02-22 05:20:17', TRUE,2,7);

-- SELECT * FROM COMENTARIO;
/* 6) Agregar el comando necesario para listar todos los artículos que tengan comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho comentario, agrupados por artículos. */

SELECT a.titulo as Titulo, a.fecha_publicacion as Fecha_Publicacion, concat(u.apellido," ",u.nombre) as ApyNom, c.fecha_hora as Fecha_Comentario
FROM articulo as a
INNER JOIN comentario as c ON a.id_articulo = c.id_articulo
INNER JOIN usuario as u ON u.id = c.id_usuario 
ORDER by c.id_articulo;





