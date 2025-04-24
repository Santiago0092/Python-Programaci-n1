import json
import datetime

# Leer archivo JSON
try:
    with open("QuizProgramación", "r") as archivo:
        datos = json.load(archivo)
except json.JSONDecodeError as e:
    print(f"Error al leer el archivo JSON: {e}")
    exit()

# Mostrar el contenido actual
print("Contenido actual del archivo JSON:")
print(json.dumps(datos, indent=4))

# Solicitar el término a buscar y el nuevo valor
termino_a_cambiar = input("Ingrese el término que desea cambiar: ").strip()
nuevo_valor = input(f"Ingrese el nuevo valor para '{termino_a_cambiar}': ").strip()

# Variable para rastrear si se encontró el término
termino_encontrado = False

# Función para buscar y reemplazar claves y valores
def buscar_y_reemplazar(diccionario, termino, nuevo_valor):
    global termino_encontrado
    for clave in list(diccionario.keys()):
        if clave == termino:
            print(f"Clave encontrada: {clave}. Reemplazando con: {nuevo_valor}")
            diccionario[nuevo_valor] = diccionario.pop(clave)
            termino_encontrado = True
            return  # Salir de la función después de reemplazar la clave

        if isinstance(diccionario[clave], dict):  # Si el valor es un diccionario, buscar recursivamente
            buscar_y_reemplazar(diccionario[clave], termino, nuevo_valor)
        elif isinstance(diccionario[clave], list):  # Si el valor es una lista, buscar en la lista
            for i in range(len(diccionario[clave])):
                if diccionario[clave][i] == termino:
                    print(f"Valor encontrado en lista: {diccionario[clave][i]}. Reemplazando con: {nuevo_valor}")
                    diccionario[clave][i] = nuevo_valor
                    termino_encontrado = True
        elif diccionario[clave] == termino:  # Si el valor coincide, reemplazar
            print(f"Valor encontrado: {diccionario[clave]}. Reemplazando con: {nuevo_valor}")
            diccionario[clave] = nuevo_valor
            termino_encontrado = True

# Llamar a la función
buscar_y_reemplazar(datos, termino_a_cambiar, nuevo_valor)

# Verificar si se encontró el término
if not termino_encontrado:
    print(f"El término '{termino_a_cambiar}' no se encontró en el JSON.")

# Agregar información adicional
datos["fecha modificada"] = str(datetime.datetime.now())

# Guardar los cambios en un archivo nuevo
try:
    with open("Actualización_Quiz.json", "w") as archivo_actualizado:
        json.dump(datos, archivo_actualizado, indent=4)
    print("El archivo JSON se ha actualizado correctamente.")
except Exception as e:
    print(f"Error al guardar el archivo JSON: {e}")
    exit()