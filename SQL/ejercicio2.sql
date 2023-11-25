/*
Ejercicio 2
Nivel de dificultad: Fácil
1. Crea una base de datos llamada "MiBaseDeDatos".
2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero).
3. Inserta dos registros en la tabla "Usuarios".
4. Actualiza la edad de un usuario en la tabla "Usuarios".
5. Elimina un usuario de la tabla "Usuarios".
Nivel de dificultad: Moderado
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto).
2. Inserta al menos tres registros en la tabla "Ciudades".
3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades".
4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN).
5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN). */

CREATE DATABASE MiBaseDeDatos;

CREATE TABLE IF NOT EXISTS usuarios(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	edad INT
)

INSERT INTO public.usuarios(nombre, edad)
VALUES
	('Andre', 32),
	('Maria', 42);

UPDATE public.usuarios
SET edad = 41
WHERE id = 2;

DELETE FROM public.usuarios
WHERE id = 2

CREATE TABLE IF NOT EXISTS ciudades(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	pais VARCHAR(255)
)

INSERT INTO public.ciudades (nombre, pais)
VALUES
	('Madrid', 'España'),
	('Rio de Janeiro', 'Brasil'),
	('Berlim', 'Alemania');

ALTER TABLE public.usuarios
ADD birthplace INT;

UPDATE public.usuarios
SET birthplace = 2
WHERE id = 1

ALTER TABLE public.usuarios
ADD CONSTRAINT FK_birthplace FOREIGN KEY (birthplace) REFERENCES ciudades(id);

SELECT usuarios.nombre, ciudades.nombre, ciudades.pais
FROM public.ciudades
LEFT JOIN public.usuarios
ON usuarios.birthplace = ciudades.id;

SELECT usuarios.nombre, ciudades.nombre, ciudades.pais
FROM public.ciudades
INNER JOIN public.usuarios
ON usuarios.birthplace = ciudades.id;
