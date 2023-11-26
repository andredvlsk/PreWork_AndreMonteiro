/* 1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),
nombre (texto) y email (texto).
2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com".
3. Actualizar el email del cliente con id=1 a "juan@gmail.com".
4. Eliminar el cliente con id=1 de la tabla "Clientes".
5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto
(texto) y cantidad (entero).
6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2.
7. Actualizar la cantidad del pedido con id=1 a 3.
8. Eliminar el pedido con id=1 de la tabla "Pedidos".
9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave
primaria), nombre (texto) y precio (decimal).
10. Insertar varios productos en la tabla "Productos" con diferentes valores.
11. Consultar todos los clientes de la tabla "Clientes".
12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los
clientes correspondientes.
13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50.
14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o
igual a 5.
15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra
"A".
Ejercicios 2
16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos
realizados por cada cliente.
17. Realizar una consulta que muestre el nombre del producto y la cantidad total de
pedidos de ese producto.
18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha.
19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla
"Productos" en la columna "producto".
20. Realizar una consulta que muestre los nombres de los clientes, los nombres de
los productos y las cantidades de los pedidos donde coincida la clave externa. */

CREATE TABLE clientes(
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	email VARCHAR(255)
)

INSERT INTO public.clientes(id, nombre, email)
VALUES (1, 'Juan', 'juan@example.com')

UPDATE public.clientes
SET email = 'juan@gmail.com'
WHERE id = 1

DELETE FROM public.clientes
WHERE id = 1

CREATE TABLE IF NOT EXISTS pedidos(
	id INT PRIMARY KEY,
	cliente_id INT NOT NULL,
	producto VARCHAR(255) NOT NULL,
	cantidad INT NOT NULL,
	CONSTRAINT FK_cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)

INSERT INTO public.pedidos(id, cliente_id, producto, cantidad)
VALUES (1, 1, 'Camiseta', 2)

/* error, porque no hay elementos en la tabla clientes
incluyendo mas clientes para poder seguir con los ejercicios */

INSERT INTO public.clientes(id, nombre, email)
VALUES
	(1, 'Rosa', 'rosa@gmail.com'),
	(2, 'Leire', 'leire@gmail.com'),
	(3, 'Andrea', 'andrea@gmail.com'),
	(4, 'Jonny', 'jonny@gmail.com'),
	(5, 'Darwin', 'darwin@gmail.com');

UPDATE public.pedidos
SET cantidad = 3
WHERE id = 1

DELETE FROM public.pedidos
WHERE id = 1

CREATE TABLE IF NOT EXISTS productos(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	precio NUMERIC
)

INSERT INTO public.productos(nombre precio)
VALUES
  ('Falda', 50.00),
  ('Sudadera', 100.00),
  ('Pantalones cortos', 20.00),
  ('Pantalones', 13.00),
  ('Vestido', 158.22),
  ('Gorra', 10.99),
  ('Camiseta', 5.10),
  ('Zapatillas', 132.90);

SELECT * FROM public.clientes
ORDER BY id ASC

/* incluyendo más pedidos para seguir con los ejercicios */

INSERT INTO public.pedidos(id, cliente_id, producto, cantidad)
VALUES
  (1, 1, 'Falda', 2),
  (2, 1, 'Sudadera', 1),
  (3, 3, 'Pantalones cortos', 3),
  (4, 4, 'Pantalones', 4);

SELECT pedidos.id, pedidos.cliente_id, pedidos.producto, pedidos.cantidad, clientes.nombre
FROM public.pedidos
LEFT JOIN public.clientes
ON pedidos.cliente_id = clientes.id;

SELECT * FROM productos
WHERE precio >= 50

SELECT * FROM pedidos
WHERE cantidad >= 5

SELECT * FROM clientes
WHERE nombre ILIKE 'A%'

SELECT clientes.nombre, SUM(pedidos.cantidad)
FROM public.clientes
LEFT JOIN public.pedidos
ON pedidos.cliente_id = clientes.id
GROUP BY nombre;

SELECT pedidos.producto, SUM(pedidos.cantidad)
FROM public.pedidos
GROUP BY producto;

ALTER TABLE public.pedidos
ADD fecha DATE;

ALTER TABLE public.pedidos
ADD CONSTRAINT FK_id FOREIGN KEY (id) REFERENCES productos(id);

select clientes.nombre, productos.nombre, pedidos.cantidad
from public.clientes
inner join public.productos
on clientes.id = productos.id
inner join public.pedidos
on pedidos.id = productos.id;