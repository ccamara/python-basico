x = 50

def func(x):
  # Vamos a cambiar el valor de x dentro de esta función
  print("x es", x) # Muestra el valor de la variable global
  x = 2 # Nueva variable local que solo existe dentro de esta función y se llama x
  print("Cambiamos la x local a", x)

func(x) 
print("x sigue siendo", x) # La variable global x no se ha alterado