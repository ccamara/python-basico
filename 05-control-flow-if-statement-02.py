number = 3
guess = int(input("Introduce un número: "))

if guess == number:
  print("Has acertado!")
else:
  #Encadenamos dentro de esta rama otra condición don dos opciones
  if guess > number:
    print("Demasiado alto")
  else:
    print("Demasiado bajo")
  print("Inténtalo de nuevo")
print("Juego terminado")