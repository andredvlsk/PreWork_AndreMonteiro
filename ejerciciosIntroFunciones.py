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