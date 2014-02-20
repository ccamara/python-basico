def area_rectang(base, height):
  '''Calcula el área de un cuadrado, a partir de dos parámetros: base y altura.
  '''
  area = base * height
  print("El area de un rectangulo de base= %d y altura= %d es: %d" %(base, height,area))

# Llamamos a la función para que calcule

# Parámetros como números
area_rectang(2,3)

# Parámetros como variables
# Las variables pueden ser las mismas que en la función u otras
base = 5  
altura = 6 
area_rectang(base,altura)

# Mostramos la documentación docstring
print(area_rectang.__doc__)