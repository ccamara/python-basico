# Sintaxis: nombre_diccionario = { llave1: valor1, llave2: valor2}
# Llave = nombre : valor = usuario de twitter
twitter_users = {"carlos": "@carlescamara", "ETSA USJ": "@etsa_usj"}
precios_software = {}  # Creamos un diccionario vacío, ya lo llenaremos más tarde

# Añadir entradas
# Llave = nombre software : valor = precio
twitter_users["USJ"] = "@_usj_"
precios_software["Autocad"] = 3000
precios_software["Blender"] = 0
precios_software["SketchupPro"] = 500
precios_software["Witbox 3D"] = 2000

print(precios_software)

# Eliminar registros
print("\nEliminamos la entrada Witbox 3D")

del precios_software["Witbox 3D"]

print(precios_software)