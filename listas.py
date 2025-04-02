
lista = [1, 'p', True, "no", 3.14, "si"]
print (type(lista))
print (lista)
numero = lista
print(numero)
decimal = lista[0]
print(decimal)
estado = lista[2]

tamaño = len(lista)
print(f"el tamaño de la lista es: {tamaño}")

estado = lista[5]
print(estado)
dato = lista[-4]
print(dato)
dato = lista[-6]
print(dato)
dato = lista[1:5]
print(dato)
#lista al contrario
dato = lista[3::-1]
print(dato)

Numeros = []
print(Numeros)
#Añadir valores a la lista
Numeros.append(10)
Numeros.append(8)
Numeros.append(5)
Numeros.append(False)
print(Numeros)
#agregar valores a la lista
Numeros.insert(0, "Johand")
print(Numeros)
Numeros.insert(2, "UNISANGIL")
print(Numeros)
Numeros.insert(-2, 6)
print(Numeros)
Numeros.append(100)
Numeros.append(1000)
Numeros.insert(5, "Celular")
Numeros.insert(3, "Crema")
print(Numeros)
#Eliminar valores de la lista
Numeros.remove(100)
print(Numeros)
Numeros.remove("Crema")
print(Numeros)
print(f"el tamaño de la lista es: {len(Numeros)}")
#Eliminar el último elemento de la lista
Numeros.pop()
print(Numeros)
print(f"el tamaño de la lista es: {len(Numeros)}")
Numeros [2:4] = []
print(Numeros)
print(f"el tamaño de la lista es: {len(Numeros)}")

for dato in Numeros:
    print(f"dato: {dato}")


Lista1 = [1, 10, 50, 20, 1000]
print(Lista1)
Lista1.reverse()
print(Lista1)
Lista1.sort()
print(Lista1)
Lista1.sort(reverse=True)
print(Lista1)

