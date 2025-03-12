Santiago = "johandMonroy"
password = 1234
print(type(password))

usuario= input("Usuario: ")
contraseña = int(input("Ingrese su contraseña: "))
print(type(contraseña))
print(Santiago == usuario and password == contraseña)
if Santiago == usuario and password == contraseña:
    print("Bienvenido")
else:
    print("Usuario o contraseña incorrectos")