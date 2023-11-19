"""Ejercicios nivel medio"""

"""1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
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
#print(result_fibo)

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
#print(result_divisores)

"""3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original."""

#3.
def unicos(lista):
  lst = []
  for elemento in lista:
    if elemento not in lst:
      lst.append(elemento)
  return lst

result_unicos = unicos([1,1,1,2,3,5,6,6,88,2,59,7])
#print(result_unicos)


"""4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos."""

#4.
def sumadigitos(n):
  totaldigitos = 0
  for i in str(n):
    totaldigitos += int(i) 
  return totaldigitos

result_sumadigitos = sumadigitos(10002)
#print(result_sumadigitos)

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
#print(result_contavocales)

"""6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista."""

#6.
def first_elements(lista, n):
  return lista[:n]

result_first_elements = first_elements(['margarita',2,'handshake',['echo',23],6,52,33], 5)
#print(result_first_elements)

"""7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena."""

#7.
def lowerupper(texto):
  contalower = 0
  contaupper = 0
  for i in texto:
    if i.islower():
      contalower += 1
    elif i.isupper():
      contaupper += 1
  return contalower, contaupper

result_lowerupper = lowerupper("HolA puEblO")
#print(result_lowerupper)

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
#print(result_numperfect)

"""9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario."""

#9.
def binary(n):
  return bin(n)[2:]

result_binary = binary(5)
#print(result_binary)

"""10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas)."""

#10.
def intersect(lista1, lista2):
  lst = []
  for l in lista1:
    if l in lista2:
      lst.append(l)
  return lst

result_intersect = intersect([1,2,3], [4,2,3])
#print(result_intersect)

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
#print(resultado_palindromo)

"""12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”."""

#12.
def fizzbuzz():
  for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
      print('FizzBuzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else:
      print(i)

#fizzbuzz()

"""13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente."""

#13.
def ascorder(lista):
  lst = sorted(lista)
  return lst

result_ascorder = ascorder([5,6,2,9,1,0,-33,88])
#print(result_ascorder)

"""14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n."""

#14.
def maslargasquen(lista, n):
  lst = []
  for palabra in lista:
    if len(palabra) > n:
      lst.append(palabra)
  return lst

result_maslargasquen = maslargasquen(['hola', 'andre', 'girafarig', 'tortilla'], 5)
#print(result_maslargasquen)

"""15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci. """

#15.
def seriefibo(n):
  if n == 0:
    return [0]
  elif n == 1:
    return [0,1]
  lista = [0,1]
  for i in range(2,n):
    lista.append(lista[i-1] + lista[i-2])
  return lista[-1]

result_seriefibo = seriefibo(10)
#print(result_seriefibo)

"""16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista."""

#16.
def mayor(lista):
  m = max(lista)
  return m

resultado_mayor = mayor([1,70,70,26,33])
#print(resultado_mayor)

"""17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo."""

#17.
def sumaalcubo(n):
  #cogiendo de la función que suma los digitos
  totaldigitosalcubo = sumadigitos(n)**3
  return totaldigitosalcubo

result_sumaalcubo = sumaalcubo(111)
#print(result_sumaalcubo)

"""18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista."""

#18.
def segundomayor(lista):
  lst_ordenada = sorted(lista, reverse=True)
  return lst_ordenada[1]

result_segundomayor = segundomayor([25,2,5,8,0,11,-3,4])
#print(result_segundomayor)


"""19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False."""

#19.
def comparalistas(lista1, lista2):
  lst = []
  for elemento in lista1:
    if elemento in lista2:
      lst.append(elemento)
  if len(lst) >= 1:
    return True
  else:
    return False

result_comparalistas = comparalistas([1,2,"hola",[8,1]], [3,6,5,[8,2],16])
#print(result_comparalistas)

"""20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso."""

#20.
def reverselista(lista):
  lst = []
  for i in range(1,len(lista)+1):
    lst.append(lista[-i])
  return lst

result_reverselista = reverselista([1,2,5,'hola','l',88,-26])
#print(result_reverselista)

"""21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene."""

def digitosletras(texto):
  contadigitos = 0
  contaletras = 0
  for i in texto:
    if i == " ":
      continue
    if i.isdigit():
      contadigitos += 1
    else:
      contaletras += 1
  return contadigitos, contaletras

result_digitosletras = digitosletras('Hola 123')
#print(result_digitosletras)

"""22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números"""

#22.
def cumsum(lista):
  csum = 0
  for i in lista:
    csum += i
  return csum

result_cumsum = cumsum([1,2,3,10])
#print(result_cumsum)

"""23. Ejercicio: Define una función que encuentre el elemento más común en una
lista."""

#23.
def mascomun(lista):
  cont = 0
  frec = 0
  for i in lista:
    rep = lista.count(i)
    if rep > cont:
      cont = rep
      frec = i
  return frec

result_mascomun = mascomun([1,2,3,3,3,10,1,1,2])
#print(result_mascomun)

"""24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10."""

#24.
def tablamultiplicar(n):
  dic = {}
  for i in range(1,11):
    dic[i] = i * n
  return dic

result_tablamultiplicar = tablamultiplicar(2)
#print(result_tablamultiplicar)

"""25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena."""

#25.
def cantidadcarac(cadena):
  dic = {}
  cont_letra = 0
  for letra in cadena:
    if letra == " ":
      continue
    else:
      dic[letra] = cadena.count(letra)
  return dic

result_cantidadcarac = cantidadcarac("bananas on the trees")
#print(result_cantidadcarac)

"""26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas."""

#26.
def notinlistas(lista1, lista2):
  lst = []
  for l in lista1:
    if l not in lista2:
      lst.append(l)
  for k in lista2:
    if k not in lista1:
      lst.append(k)
  return lst

result_notinlistas = notinlistas([1,2,3,20,'Hola'], [4,2,3,6])
#print(result_notinlistas)

"""27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados."""

#############27 IGUAL A LA NUMERO 3############## 

"""28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número."""

#28.
def sumacuadradospares(n):
  somacuadrados = 0
  contador = 0
  while contador <= n:
    if contador % 2 == 0:
      somacuadrados += contador**2
    contador += 1
  return somacuadrados

result_somacuadradospares = sumacuadradospares(6)
#print(result_somacuadradospares)

"""29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista."""

#29.
def promedio(lista):
  total = 0
  for numeros in lista:
    total += numeros
  return total / len(lista)

result_promedio = promedio([100,80,30])
#print(result_promedio)

"""30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista."""

#30.
def maslarga(lista):
  dic = {}
  for texto in lista:
    dic[texto] = len(texto)
  larga = max(dic, key = dic.get)
  return larga

#siempre retorna el 1er mayor.
result_maslarga = maslarga(['hola','girafarig', 'tortillas'])
#print(result_maslarga)

"""31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos."""

#31.
#cogiendo la función que identifica si es primo o no
def primo(p):
  if p <= 1:
    return False
  for i in range(2, p):
    if p % i == 0:
      return False
  return True

def printprimos(n):
  lst = []
  for i in range (0,n+1):
    if primo(i) == True:
      lst.append(i)
  return lst

result_printprimos = printprimos(100)
print(result_printprimos)

"""32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso."""

#32.
def ordeninverso(texto):
  palabras = texto.split(" ")
  rev = ' '.join(reversed(palabras))
  return rev

result_ordeninverso = ordeninverso('bananas on the trees')
#print(result_ordeninverso)

"""33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla."""

#33.
#para utilizar el parametro key de la función sorted, se necesita una función adicional para el orden.
def ultimo(ult):
  return ult[-1]

def orderlast(list_of_tuples):
  order = sorted(list_of_tuples, key=ultimo)
  return order

result_orderlast = orderlast([(1,2), (3,4), (2,2), (1,3,1), (2,1,1)])
#print(result_orderlast)

"""34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena."""

#34.
################Igual al ejercicio numero 5.#######################

"""35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False."""

#35.
def primoint(p):
  if p <= 1:
    return False
  for i in range(2, p):
    if p % i == 0:
      return False
    else:
      return True
    
result_primoint = primoint(12)
#print(result_primoint)