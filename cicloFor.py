# Ciclo for
numero = float(input("Ingrese un número para multiplicar: "))
for i in range(1, 10, 2):
    print(i)

x = "Ayuda"

#separar caracteres
for arroz in x:
    if arroz == "d":
        break
    else:
       print(arroz)
       #tabla de multiplicar
for mul in range(1, 11):
    print(f"{numero} x {mul} = {numero*mul}")

for pares in range(1, 10):
    if pares % 2 == 0:
        print(pares, "es par")
        
    else:
        print(pares, "es impar")
       