import re

def ejercicio1():
    print("--------------")
    print("Ingrese la matricula de aerolinea:")
    print("")
    matricula = str(input())
    if re.match(r"((LV-SX\d{3})|(LV-S\d{3})|(LV-X\d{3})|(LQ-[A-Z]{3})|(LV-[A-Z]{3}))$", matricula):
        print("La matricula es valida!")
    else:
        print("La matricula no es valida!")
    print("")
    print("--------------")
    print("")

def ejercicio2():
    print("--------------")
    print("Ingrese un numero menor a 1900:")
    print("")
    numero = str(input())
    if re.match(r"^(([0-9]{1,3})|([1]([0-8])\d\d))$", numero):
        print("El numero es valido!")
    else:
        print("El numero no es valido!")
    print("")
    print("--------------")
    print("")

def mostrar_menu():
    print("Elija el ejercicio que quiere ejecutar")
    print("1 - Validacion de codigo de aerolineas")
    print("2 - Validacion de numero menor a 1900")
    print("0 - Salir")

mostrar_menu()
eleccion = int(input())

while eleccion != 0:
    if eleccion == 1:
        ejercicio1()
    if eleccion == 2:
        ejercicio2()
    mostrar_menu()
    eleccion = int(input())
