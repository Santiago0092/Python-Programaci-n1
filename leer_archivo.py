import json
#leer el archivo json
archivo = open("", "r")
#guardar json
datos = json.load(archivo)
#imprimir el archivo

print(datos)

#cerrar el archivo
archivo.close()
