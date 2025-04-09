estudiantes = {
        "Estudiante": [
        {
        "Nombre": "José",
        "apellido": "Moreno",
        "cedula": 3123222131}],

        "estudiante2": [{
        "Nombre": "Tomás",
        "apellido": "Merchán",
        "celular": 3121231}],

        "estudiante3": [{
        "Nombre": "Haider",
        "apellido": "Machado",
        "celular": 103222131}]

        
   }
   



Diccionario = {
    "Nombre": "santiago",
    "celular": 31232131,
    "universidad": "unisangil",
    "estado": True,  # Corrected to a boolean
    "Estatura": 1.70,
    "Edad": 18,
    "lista": ["1", "2", "3", "4", "5"]
}

# Tipo de dato




programacion ={
 
    "Nombre": "santiago",
    "apellido": "Monroy",
    "celular": 31232131,
    "universidad": "unisangil",
    "correo": "santiago@gmail.com",
    "estado": "True",
    "Estatura": 1.70,
    "Edad": 18,
    "lista": ["1", "2", "3", "4", "5"],
    "direccion": "calle 22A #4-33 urb primavera",
    "Lista2": ["Arroz", "Frijoles", "Lentejas"]
}

# Acceder a los valores del diccionario
print(Diccionario)
print(programacion)
print(programacion["Nombre"])

for estudiante in estudiantes["Estudiante"]:
    print(estudiante["Nombre"])
    print(estudiante["apellido"])
    print(estudiante["cedula"])

    print(programacion.items())
    for estudiante in estudiantes["Estudiante"]:
      print((estudiantes.keys()))
    print((Diccionario.keys()))  

    print((Diccionario.get("estado")))
    print((Diccionario.get("universidad")))

    #agregar informacion a un diccionario
    programacion["programa"] = "ingeniera de sistemas"

    print(programacion)

    estudiantes["Estudiante4"] = "nombre" "Juan"

    print (estudiantes)

