number = 23
guess = int(input('Enter an integer : '))

if guess == number:
  print('Congratulations, you guessed it.') # Inicio de nuevo bloque
  print('(but you do not win any prizes!)') # Fin de nuevo bloque
elif guess < number:
  print('No, it is a little higher than that') # Otro bloque
  # Puedes hacer lo que quieras en un bloque ...
else:
  print('No, it is a little lower than that')
  # Este bloque se muestra cuando el intento es mayor que el número (guess > number)

print('Done')
# This last statement is always executed, after the if statement is executed

# Fuente: A Byte of Python.