def maximum(x, y):
  if x > y:
    return x
  elif x == y:
    return "Los números son iguales"
  else:
    return y
  print("Esto no debería ejecutarse nunca")
  # No se ejecuta porque las tres opciones anteriores fuerzan la salida de la función
  
print(maximum(2, 3))
