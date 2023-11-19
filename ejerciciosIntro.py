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


"""Funciones
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""

#1.
def sumar(a, b):
  suma = a + b
  return(suma)

resultado = sumar(22, -20)
print(resultado)

#2.
def factorial(a):
  fac = 0
  total = 1
  for i in range(1,a + 1):
    fac = total * (a - i)
    total += fac
  return(total)

factor = factorial(5)
print(factor)

#3.
def primo(p):
  if p <= 1:
    return "No primo"
  for i in range(2, p):
    if p % i == 0:
      return "No primo"
    else:
      return "Primo"

resultado_primo = primo(11)
print(resultado_primo)

#4.
def listsum(lista):
  sumofnumbers = 0
  for numbers in lista:
    sumofnumbers += numbers
  return sumofnumbers

resultado_listsum = listsum([1,2,3,4])
print(resultado_listsum)

#5.
def cadena_reversa(texto):
  reverso = ''
  for i in range(1,len(texto)+1):
    reverso += texto[-i]
  return reverso

resultado_cadena_reversa = cadena_reversa('works fine!')
print(resultado_cadena_reversa)

"""Ejercicios nivel medio

1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci."""

#1.
def fibo(n):
  if n == 0:
    return [0]
  elif n == 1:
    return [0,1]
  lista = [0,1]
  for i in range(2,n):
    lista.append(lista[i-1] + lista[i-2])
  return lista

result_fibo = fibo(10)
print(result_fibo)

"""2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores."""

#2.
def divisores(n):
  lista = []
  for i in range(1,n+1):
    if n % i == 0:
      lista.append(i)
  return lista

result_divisores = divisores(20)
print(result_divisores)

"""3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original."""

"""4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos."""

#4.
def sumadigitos(n):
  totaldigitos = 0
  for i in str(n):
    totaldigitos += int(i) 
  return totaldigitos

result_sumadigitos = sumadigitos(10002)
print(result_sumadigitos)

"""5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena."""

#5.
def contavocales(texto):
  conta = 0
  vocales = ['a','e','i','o','u']
  for v in vocales:
    for letra in texto:
      if v == letra:
        conta +=1
      else:
        conta +=0
  return conta

result_contavocales = contavocales('cuenta las vocales de una cadena de texto')
print(result_contavocales)

"""6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista."""

#6.
def first_elements(lista, n):
  return lista[:n]

result_first_elements = first_elements(['margarita',2,'handshake',['echo',23],6,52,33], 5)
print(result_first_elements)

"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena."""

"""8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3."""

#8.
def numperfect(n):
  lista = []
  for i in range(1,n): #quitar el +1 para poder no aparecer el n en la lista.
    if n % i == 0:
      lista.append(i)
  total = 0
  for l in lista:
    total += l
  if total == n:
    return True
  else:
    return False

result_numperfect = numperfect(28)
print(result_numperfect)

"""9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario."""

"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas)."""

"""11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""

#11.
def palindromo(cadena_texto):
  reverso = ''
  for i in range(1,len(cadena_texto)+1):
    reverso += cadena_texto[-i]
  if cadena_texto.lower() == reverso.lower():
    return "PALINDROMO"
  else:
    return "NO PALINDROMO"

resultado_palindromo = palindromo('Girafarig')
print(resultado_palindromo)

"""12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”."""

"""
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente."""

#13.
def ascorder(lista):
  lst = sorted(lista)
  return lst

result_ascorder = ascorder([5,6,2,9,1,0,-33,88])
print(result_ascorder)

"""14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False."""