usuario = "Santiago"
contraseña = 5656 
intentos = 3
saldo = 0

user = input("Ingrese su usuario: ")
contra = int(input("Ingrese su contraseña: "))

while usuario != user or contraseña != contra:
    print("Usuario o contraseña inválidos")
    intentos -= 1
    print("Intentos restantes:", intentos)
    if intentos < 1:
        print("Se ha bloqueado el acceso")
        break
    user = input("Ingrese su usuario: ")
    contra = int(input("Ingrese su contraseña: "))

if usuario == user and contraseña == contra:
    print("Bienvenido al cajero")
    while True:
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = int(input("Ingrese una opción (número): "))
        
        if opcion == 1:
            print("Su saldo es: ", saldo)
        elif opcion == 2:
            deposito = int(input("Ingrese el valor a depositar: "))
            saldo += deposito
            print("Se ha hecho su depósito")
            print("Su saldo es: ", saldo)
        elif opcion == 3:
            dinerog = int(input("Ingrese el valor a retirar: "))
            if dinerog <= saldo:
                saldo -= dinerog
                print("Se ha hecho su retiro")
                print("Su saldo es: ", saldo)
                if dinerog > saldo:
                    print("No tiene suficiente saldo")
        elif opcion == 4:
            print("Gracias por usar el cajero")
            break
   
        



