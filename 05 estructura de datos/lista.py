# Ejemplo copiado de A Byte of Python.
# Mi lista de la compra
shoplist = ["manzana", "mango", "zanahoria", "banana"]

# Contar elementos de la lista
print("Tengo", len(shoplist), "elementos para comprar")

# Listar elementos de la lista
print("Estos elementos son:")
for item in shoplist:
      print(item)

print("\nTambién tengo que comprar arroz")
# Añadimos un nuevo item a la lista.
shoplist.append("arroz")
print("Mi lista de la compra está formada por:", shoplist)

# Ordenar los elementos de la lista
print("Voy a ordenar los elementos de la lista")
shoplist.sort()
print("La lista ordenada de la compra es", shoplist)

# Mostrar el primer elemento de la lista.
print("El primer item que voy a comprar es", shoplist[0]) 
olditem = shoplist[0]
del shoplist[0]
print("He comprado el", olditem)
print("Mi lista de la compra ahora es:", shoplist)
