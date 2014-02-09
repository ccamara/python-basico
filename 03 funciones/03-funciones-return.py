def maximum(x, y):
  if x > y:
    return x
  elif x == y:
    return "Los números son iguales"
  else:
    return y
  print("Esto no debería ejecutarse nunca")
  # No se ejecuta porque las tres opciones anteriores fuerzan la salida de la función
  # Solo se ejecutaría si alguna de las opciones anteriores tuviese un print en lugar de return
  
print(maximum(2, 3))
