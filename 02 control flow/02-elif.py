guess = int(input("Introduce un número: "))
number = 3

if number == guess:
    print("Has acertado!")
elif guess > number:
    print("Demasiado alto")
    print("Inténtalo de nuevo")
else:
    print("Demasiado bajo")
    print("Inténtalo de nuevo")
print("Juego terminado")