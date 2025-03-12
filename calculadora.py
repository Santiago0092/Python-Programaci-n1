import math
while True:
    print(" Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Salir")
    opcion = int(input("Ingrese una opción (número): "))
    if opcion == 7:
        print("Gracias por usar la calculadora")
        break
    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print ("La suma es: ", num1 + num2)
    if opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        rta = num1 - num2
        print ("La resta es: ", rta)
        
    if opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print ("La multiplicación es: ", num1 * num2)
    if opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        rta = num1 / num2
        print ("La división es: ", rta)
    if opcion == 5:
        num1 = float(input("Ingrese el número: "))
        num2 = float(input("Ingrese la potencia: "))
        rta = num1 ** num2
        print ("La potencia es: ", rta)
    if opcion == 6:
        num1 = float(input("Ingrese el número: "))
        rta = math.sqrt(num1)
        print ("La raiz es: ", rta)
