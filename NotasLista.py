lista = []
for i in range(8):
        materia = input("Ingrese la materia: ") 
        nota = float(input("Ingrese la nota: "))
        # Agregar materia y nota a la lista
        lista.append(materia, nota)    
print("Lista final:", lista)

for dato in lista:
    print(f"dato: {dato}")
