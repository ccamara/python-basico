x = 50

def func(x):
  # Vamos a cambiar el valor de x dentro de esta función
  print("x es", x) # Muestra el valor del parámetro, que en este caso se llama x
  x = 2 # Nueva variable local que solo existe dentro de esta función y se llama x
  print("Cambiamos la x local a", x)

func(x) 
print("x sigue siendo", x) # La variable global x no se ha alterado

''' 
Ejemplo de variables globales
'''
x = 50

def func():
    global x # Indicamos que x se ha definido fuera de la función
    print("x es", x) # Mostramos el valor inicial de x
    x = 2 # Asignamos un nuevo valor a la x global
    print("Cambiamos la x global a", x)
    
func()
print("Ahora el valor de x es", x)