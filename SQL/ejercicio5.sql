/*
Ejercicio 5
1. Crea una tabla llamada "Clientes" con las columnas id (entero) y nombre
(cadena de texto).
2. Inserta un cliente con id=1 y nombre='John' en la tabla "Clientes".
3. Actualiza el nombre del cliente con id=1 a 'John Doe' en la tabla "Clientes".
Ejercicios 4
4. Elimina el cliente con id=1 de la tabla "Clientes".
5. Lee todos los clientes de la tabla "Clientes".
6. Crea una tabla llamada "Pedidos" con las columnas id (entero) y cliente_id
(entero).
7. Inserta un pedido con id=1 y cliente_id=1 en la tabla "Pedidos".
8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos".
9. Elimina el pedido con id=1 de la tabla "Pedidos".
10. Lee todos los pedidos de la tabla "Pedidos".
11. Crea una tabla llamada "Productos" con las columnas id (entero) y nombre
(cadena de texto).
12. Inserta un producto con id=1 y nombre='Camisa' en la tabla "Productos".
13. Actualiza el nombre del producto con id=1 a 'Pantalón' en la tabla "Productos".
14. Elimina el producto con id=1 de la tabla "Productos".
15. Lee todos los productos de la tabla "Productos".
16. Crea una tabla llamada "DetallesPedido" con las columnas pedido_id (entero) y
producto_id (entero).
17. Inserta un detalle de pedido con pedido_id=1 y producto_id=1 en la tabla
"DetallesPedido".
18. Actualiza el producto_id del detalle de pedido con pedido_id=1 a 2 en la tabla
"DetallesPedido".
19. Elimina el detalle de pedido con pedido_id=1 de la tabla "DetallesPedido".
20. Lee todos los detalles de pedido de la tabla "DetallesPedido".
21. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un inner join.
22. Realiza una consulta para obtener todos los clientes y sus pedidos
correspondientes utilizando un left join.
23. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un inner join.
24. Realiza una consulta para obtener todos los productos y los detalles de pedido
correspondientes utilizando un left join.
Ejercicios 5
25. Crea una nueva columna llamada "telefono" de tipo cadena de texto en la tabla
"Clientes".
26. Modifica la columna "telefono" en la tabla "Clientes" para cambiar su tipo de
datos a entero.
27. Elimina la columna "telefono" de la tabla "Clientes".
28. Cambia el nombre de la tabla "Clientes" a "Usuarios".
29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a
"nombre_completo".
30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios".
*/


create table clientes(
	id INT,
	nombre VARCHAR(255)
)

insert into public.clientes (id, nombre)
values (1, 'John');

update public.clientes
set nombre = 'John Doe'
where id = 1;

delete from public.clientes
where id = 1;

select * from public.clientes

create table pedidos(
  id INT,
  cliente_id INT
)

insert into public.pedidos (id, cliente_id)
values (1, 1);

update public.pedidos
set cliente_id = 2
where id = 1;

delete from public.pedidos
where id = 1;

select * from public.pedidos

create table productos(
  id INT,
  nombre VARCHAR(255)
)

insert into public.productos(id, nombre)
values(1, 'Camisa');

update public.productos
set nombre = 'Pantalón'
where id = 1;

delete from public.productos
where id = 1;

select * from public.productos

create table detallespedido(
  pedido_id INT,
  producto_id INT
)

insert into public.detallespedido(pedido_id, producto_id)
values (1,1);

update public.detallespedido
set producto_id = 2
where pedido_id = 1;

delete from public.detallespedido
where pedido_id = 1;

select * from public.detallespedido;

select clientes.id, clientes.nombre, pedidos.id
from public.clientes
inner join public.pedidos
on clientes.id = pedidos.cliente_id;

select clientes.id, clientes.nombre, pedidos.id
from public.clientes
left join public.pedidos
on clientes.id = pedidos.cliente_id;

select productos.id, productos.nombre, detallespedido.pedido_id
from public.productos
inner join public.detallespedido
on productos.id = detallespedido.producto_id;

select productos.id, productos.nombre, detallespedido.pedido_id
from public.productos
left join public.detallespedido
on productos.id = detallespedido.producto_id;

alter table public.clientes
add telefono VARCHAR(255);

alter table public.clientes
alter column telefono type INT
using telefono::integer;

alter table public.clientes
drop column telefono;

alter table public.clientes
rename to usuarios;

alter table public.usuarios
rename column nombre to nombre_completo;

alter table public.usuarios
add primary key (id);