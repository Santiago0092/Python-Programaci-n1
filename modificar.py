import json
import datetime
#leer archivo
archivo = open("informacion_json", "r")
#guardar json
datos = json.load(archivo)
#imprimir el archivo
print(datos)
#cerrar el archivo
archivo.close()

username = input("Ingrese su nombre de usuario: ")
datos["usario"] = username
datos["fecha modificada"] = str (datetime.datetime.now())
#guardar archivo
archivo = open("informacion_actualizadajson", "w")
#escribir el archivo
json.dump(datos, archivo)
#cerrar el archivo
archivo.close()
