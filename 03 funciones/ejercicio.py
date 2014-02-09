from random import randint # Importamos la función randint
secret = randint(1, 10) # Generamos un número aleatorio del 1 al 10

print("¿Qué número crees que he elegido?")
guess = input("Escribe un número del 1 al 10: ")
count = 1
valid = True

def attempt():
  global count 
  count = count + 1
  global guess
  guess = int(input("Escribe un número del 1 al 10: "))

def guess_validation():
  global guess
  global valid
  if guess.isdigit():
    valid = True
  else:
    # Si la condición no se cumple es que hay algo que no son números
    valid = False


guess_validation()

# Verificamos que guess no contenga carácteres no numéricos

if valid == False:
  print("Solo puedes escribir números enteros")
  
else:
  while guess != 0 and valid == True:
    guess = int(guess) # Convertimos guess en un número
    while guess != secret:
      if guess > 10:
        print("El número elegido no está entre 1 y 10")
        attempt()
        continue
      else:
        if guess > secret:
          print("Demasiado alto, inténtalo de nuevo")
          attempt()
          continue
        else:
          print("Demasiado bajo")
          attempt()
          continue
    print("¡Enhorabuena!, lo has conseguido en " + str(count) + " intentos")
    break


