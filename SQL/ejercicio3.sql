/*
Ejercicios 3
1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico).
2. Inserta al menos cinco registros en la tabla "Productos".
3. Actualiza el precio de un producto en la tabla "Productos".
4. Elimina un producto de la tabla "Productos".
5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").
*/

CREATE TABLE IF NOT EXISTS productos(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	precio NUMERIC
)

INSERT INTO public.productos(nombre, precio)
VALUES
	('Patata', 2.10),
	('Aceite', 7.30),
	('Cebolla', 1.20),
	('Té', 0.80),
	('Café', 3.15);

UPDATE public.productos
SET precio = 4.22
WHERE nombre = 'Café'

DELETE from public.productos
WHERE nombre = 'Té'

ALTER TABLE public.usuarios
ADD producto_comprado INT

UPDATE public.usuarios
SET producto_comprado = 2
WHERE id = 1;

ALTER TABLE public.usuarios
ADD CONSTRAINT FK_producto_comprado FOREIGN KEY (producto_comprado) REFERENCES productos(id);

SELECT usuarios.nombre, productos.nombre
FROM public.productos
INNER JOIN public.usuarios
ON usuarios.producto_comprado = productos.id;