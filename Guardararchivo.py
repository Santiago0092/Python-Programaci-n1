import json
#crear un archivo json
#crear diccionario
datos = {
  "Nombre": "santiago",
    "apellido": "Monroy",
    "celular": 31232131,
    "universidad": "unisangil",
    "correo": "santiago@gmail.com",
    "estado": "True",
    "Estatura": 1.70,
    "Edad": 18
}
#variable para guardar el archivo
archivo = open("informacion_json", "w")
#escribir el archivo
json.dump(datos, archivo)

#cerrar el archivo
archivo.close() 
