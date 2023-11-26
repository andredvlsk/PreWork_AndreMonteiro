/*
Ejercicio 4
Nivel de dificultad: Experto
1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").
2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos.
3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).
4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).
5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)
*/

CREATE TABLE pedidos(
	id INT PRIMARY KEY,
	id_usuario INT ,
	id_producto INT,
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	FOREIGN KEY (id_producto) REFERENCES productos(id)
)

INSERT INTO pedidos (id, id_usuario, id_producto)
VALUES 
	(1, 3, 2),
	(2, 1, 5),
	(3, 1, 3),
	(4, 1, 1);

SELECT usuarios.nombre, coalesce(productos.nombre,'NA')
FROM public.usuarios
LEFT JOIN public.productos
ON usuarios.producto_comprado = productos.id

SELECT usuarios.nombre
FROM public.usuarios
LEFT JOIN public.pedidos
ON usuarios.id = pedidos.id_usuario
GROUP BY usuarios.nombre

ALTER TABLE public.pedidos
ADD cantidad NUMERIC;

UPDATE public.pedidos
SET cantidad = 1
WHERE id = 1;

UPDATE public.pedidos
SET cantidad = 10
WHERE id = 2;

UPDATE public.pedidos
SET cantidad = 3.5
WHERE id = 3;

UPDATE public.pedidos
SET cantidad = 5
WHERE id = 4;