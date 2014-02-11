from random import randint # Importamos la función randint
secret = randint(1, 10) # Generamos un número aleatorio del 1 al 10

print("¿Qué número crees que he elegido?")
guess = input("Escribe un número del 1 al 10: ")
count = 1

# Verificamos que guess no contenga carácteres no numéricos
if guess.isdigit():
  guess = int(guess) # Convertimos guess en un número
  while guess != secret:
    if guess > 10:
      print("El número elegido no está entre 1 y 10")
      count = count + 1
      guess = int(input("Escribe un número del 1 al 10: "))
    else:
      if guess > secret:
        print("Demasiado alto, inténtalo de nuevo")
        count = count + 1
        guess = int(input("Escribe un número del 1 al 10: "))
      else:
        print("Demasiado bajo")
        count = count + 1
        guess = int(input("Escribe un número del 1 al 10: "))
  print("¡Enhorabuena!, lo has conseguido en " + str(count) + " intentos")

else:
  # Si la condición no se cumple es que hay algo que no son números
  print("Solo puedes escribir números enteros")
  count = count +1
  guess = input("Escribe un número del 1 al 10: ")
