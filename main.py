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

def mostrar_menu():
    print("Elija el ejercicio que quiere ejecutar")
    print("1 - Validacion de codigo de aerolineas")
    print("0 - Salir")

mostrar_menu()
eleccion = int(input())

while eleccion != 0:
    if eleccion == 1:
        ejercicio1()
    mostrar_menu()
    eleccion = int(input())
