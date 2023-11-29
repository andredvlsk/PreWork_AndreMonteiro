#Calculadora

def sumar(x, y):
  return x + y

def restar(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
  return x / y

def expon(x, y):
  return x ** y

def calculadora():
  print("¡Bienvenido a la Calculadora!")
  while True:
    eleccion_de_operación = input('Selecciona una operación (Sumar/Restar/Multiplicar/Dividir/Expo) o Salir para salir de la calculadora: ')
    lista_operaciones = ['Sumar', 'Restar', 'Multiplicar', 'Dividir', 'Expo']
    if eleccion_de_operación == 'Salir':
      print('Gracias por utilizar la calculadora.')
      break
    elif eleccion_de_operación not in lista_operaciones:
      print ('Opción inválida')
      break
    elif eleccion_de_operación in lista_operaciones:
      x = int(input('Digite o primeiro numero: '))
      y = int(input('Digite o segundo numero: '))
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