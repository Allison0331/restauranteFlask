--  Creado con Kata Kuntur - Modelador de Datos
--  Versión: 2.9.1
--  Sitio Web: http://katakuntur.jeanmazuelos.com/
--  Si usted encuentra algún error le agradeceriamos lo reporte en:
--  http://pm.jeanmazuelos.com/katakuntur/issues/new

--  Administrador de Base de Datos: SQLite
--  Diagrama: restaurante_misiontic
--  Autor: diani
--  Fecha y hora: 21/10/2021 20:45:44
PRAGMA foreign_keys = ON;

-- GENERANDO TABLAS
CREATE TABLE usuarios (
	tipo_identificacion VARCHAR NOT NULL ,
	identificacion INTEGER NOT NULL ,
	nombres VARCHAR NOT NULL ,
	apellidos VARCHAR NOT NULL ,
	fecha_nacimiento DATE NOT NULL ,
	direccion VARCHAR NOT NULL ,
	telefono INTEGER NOT NULL ,
	email VARCHAR NOT NULL ,
	nombre_usuario VARCHAR NOT NULL ,
	contrasena VARCHAR NOT NULL ,
	nivel_acceso INTEGER NOT NULL ,
	estado BOOL NOT NULL ,
	PRIMARY KEY(identificacion)
);
CREATE TABLE productos (
	codigo VARCHAR NOT NULL ,
	nombre VARCHAR NOT NULL ,
	valor_unitario DOUBLE NOT NULL ,
	estado VARCHAR NOT NULL ,
	categoria VARCHAR NOT NULL ,
	descripcion VARCHAR NOT NULL ,
	url VARCHAR NOT NULL ,
	PRIMARY KEY(codigo)
);
CREATE TABLE comentarios (
	id INTEGER NOT NULL ,
	codigo_producto VARCHAR NOT NULL ,
	id_cliente INTEGER NOT NULL ,
	comentario VARCHAR NOT NULL ,
	calificacion_producto INTEGER NOT NULL ,
	productos_codigo VARCHAR NOT NULL ,
	usuarios_identificacion INTEGER NOT NULL ,
	FOREIGN KEY (productos_codigo) REFERENCES productos(codigo),
	FOREIGN KEY (usuarios_identificacion) REFERENCES usuarios(identificacion),
	PRIMARY KEY(id)
);
CREATE TABLE pedidos (
	codigo_pedido VARCHAR NOT NULL ,
	fecha DATE NOT NULL ,
	id_cliente INTEGER NOT NULL ,
	observaciones VARCHAR NOT NULL ,
	estado_pedido VARCHAR NOT NULL ,
	valor_total DOUBLE NOT NULL ,
	impuesto DOUBLE NOT NULL ,
	descuento DOUBLE NOT NULL ,
	usuarios_identificacion INTEGER NOT NULL ,
	FOREIGN KEY (usuarios_identificacion) REFERENCES usuarios(identificacion),
	PRIMARY KEY(codigo_pedido)
);
CREATE TABLE detalle_pedidos (
	codigo_pedido VARCHAR NOT NULL ,
	codigo_producto VARCHAR NOT NULL ,
	cantidad INTEGER NOT NULL ,
	valor_total_producto INTEGER NOT NULL ,
	pedidos_codigo_pedido VARCHAR NOT NULL ,
	productos_codigo VARCHAR NOT NULL ,
	FOREIGN KEY (pedidos_codigo_pedido) REFERENCES pedidos(codigo_pedido),
	FOREIGN KEY (productos_codigo) REFERENCES productos(codigo)
);
CREATE TABLE lista_deseos (
	id_usuario INTEGER NOT NULL ,
	codigo_producto VARCHAR NOT NULL ,
	usuarios_identificacion INTEGER NOT NULL ,
	productos_codigo VARCHAR NOT NULL ,
	FOREIGN KEY (usuarios_identificacion) REFERENCES usuarios(identificacion),
	FOREIGN KEY (productos_codigo) REFERENCES productos(codigo)
);