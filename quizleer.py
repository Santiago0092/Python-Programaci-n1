import json
#leer el archivo json
archivo = open("QuizProgramación", "r")
#guardar json
datos = json.load(archivo)
#imprimir el archivo


#cerrar el archivo
archivo.close()
