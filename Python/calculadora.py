#Calculadora

def sumar(x, y):
  return x + y

def restar(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
  if y != 0:
    return x / y
  else:
    return "MATH ERROR"

def expon(x, y):
  return x ** y

def raiz_cuad(x):
  if x > 0:
    return x ** 0.5
  else:
    return "MATH ERROR"

def calculadora():
  print("¡Bienvenido a la Calculadora!")
  while True:
    eleccion_de_operación = input('Selecciona una operación (Sumar/Restar/Multiplicar/Dividir/Expo/Raiz) o Salir para salir de la calculadora: ')
    lista_operaciones = ['Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Expo', 'Raiz']
    if eleccion_de_operación == 'Salir':
      print('Gracias por utilizar la calculadora.')
      break
    elif eleccion_de_operación not in lista_operaciones:
      print (f'{eleccion_de_operación} es una opción inválida')
      ### se puede incluir un control para que cuando el usuario introduzca letras en vez de numeros en x e y que salte un mensaje de error
    elif eleccion_de_operación in lista_operaciones:
      if eleccion_de_operación == 'Raiz':
        x = int(input('Type number to square root: '))
        print(raiz_cuad(x))
      else:
        x = int(input('Type first number: '))
        y = int(input('Type second number: '))
        if eleccion_de_operación == 'Sumar':
          print(sumar(x,y))
        if eleccion_de_operación == 'Restar':
          print(restar(x,y))
        if eleccion_de_operación == 'Dividir':
          print(dividir(x,y))
        if eleccion_de_operación == 'Multiplicar':
          print(multiplicar(x,y))
        if eleccion_de_operación == 'Expo':
          print(expon(x,y))


if __name__ == "__main__":
  calculadora()