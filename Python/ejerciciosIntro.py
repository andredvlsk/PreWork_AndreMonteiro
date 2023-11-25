"""
Variables y Operadores
1. Ejercicio: Crea una variable llamada nombre y asígnale tu nombre como valor.
Luego, imprime la variable.
2. Ejercicio: Crea dos variables, a y b , y asígnales los valores 5 y 10
respectivamente. Luego, imprime la suma de a y b .
3. Ejercicio: Calcula el área de un triángulo con base 10 y altura 5.
4. Ejercicio: Calcula el resto de dividir 17 entre 3."""

#1.
nombre = 'Andre'
print(nombre)

#2.
a = 5
b = 10
print(a + b)
 
#3.
b = 10
h = 5
areatriangulo = (b * h) / 2
print(areatriangulo)

#4.
resto = 17 % 3
print(resto)


"""Condicionales
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos."""

#1.
n = -4
if n > 0:
  print('Positivo')
else:
  print('Negativo')

#2.
if n % 2 == 0:
  print('Par')
else:
  print('Impar')

#3.
i = 50
j = 50
k = 32
m = max(i,j,k)
print(m)

"""Bucles
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100."""

#1.
for numero in range(1,11):
  print(numero)

#2.
i = 1
while i <= 20:
  if i % 2 == 0:
    print(i)
  i+=1 

#3.
suma = 0
for i in range(1,101):
  suma +=i

print(suma)