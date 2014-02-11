print ("¿Hemos llegado ya?")
 
answer = "No"
 
while answer != "sí":
  print("¿Y ahora?")
  answer = input()
  # Como Sí = sí, lo pasamos a minúsculas para que no haya distinción
  answer = answer.lower()
print("¡Qué bien!")