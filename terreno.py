import math
#terreno
base = float(input("ingrese la base del terreno: "))
Altura = float(input("ingrese la altura del terreno - triangulo: "))
Altura2 = float(input("ingrese la altura del terreno - rectangulo: "))
lado = float(input("ingrese el lado del terreno: "))
#operaciones 
Triangulo= (base*Altura)/2
print(f"el area del triangulo es: {Triangulo}")
Rectangulo= base*Altura2
print(f"el area del rectangulo es: {Rectangulo}")
area_total= Triangulo+Rectangulo
print(f"el area total del terreno es: {area_total}")


