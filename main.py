import re
import json


def ejercicio1():
    print("--------------")
    print("Ingrese la matricula de aerolinea:")
    print('')
    matricula = str(input())
    if re.match(r"((LV-SX\d{3})|(LV-S\d{3})|(LV-X\d{3})|(LQ-[A-Z]{3})|(LV-[A-Z]{3}))$", matricula):
        print("La matricula es valida!")
    else:
        print("La matricula no es valida!")
    print('')
    print("--------------")
    print('')


def ejercicio2():
    print("--------------")
    print("Ingrese un numero menor a 1900:")
    print('')
    numero = str(input())
    if re.match(r"^(([0-9]{1,3})|([1]([0-8])\d\d))$", numero):
        print("El numero es valido!")
    else:
        print("El numero no es valido!")
    print('')
    print("--------------")
    print('')


def ejercicio3():
    print("--------------")
    print("Ingrese el nombre de la estacion:")
    print('')
    nombre = str(input())
    archivo = open('estaciones.json',)
    estaciones = json.load(archivo)
    archivo.close()
    for estacion in estaciones:
        print('---------------')
        if estacion['nombre'] == nombre:
            print(f"Cantidad de sensores de la estación “{estacion['nombre']}”: {len(estacion['sensores'])}")
            for sensor in estacion['sensores']:
                print(f"{sensor['nombre']}: {sensor['medicion']}{sensor['unidad']}")
            print('')
            return
        print('---------------')
    print('')
    print("No se ha encontrado la estacion con el nombre seleccionado")
    print('')


def ejercicio4():
    archivo = open('estaciones.json',)
    estaciones = json.load(archivo)
    ordenadas = sorted(estaciones, key=lambda estacion: sum(estacion['bateria']) / len(estacion['bateria']))
    print('')
    print(f"La estacion con menos bateria es: {ordenadas[0]['nombre']}")
    print('')
    archivo.close()


def mostrar_menu():
    print("Elija el ejercicio que quiere ejecutar")
    print("1 - Validacion de codigo de aerolineas")
    print("2 - Validacion de numero menor a 1900")
    print("3 - Obtener informacion de estacion")
    print("4 - Calcular estacion con menos bateria")
    print("0 - Salir")


mostrar_menu()
eleccion = int(input())

while eleccion != 0:
    if eleccion == 1:
        ejercicio1()
    if eleccion == 2:
        ejercicio2()
    if eleccion == 3:
        ejercicio3()
    if eleccion == 4:
        ejercicio4()
    mostrar_menu()
    eleccion = int(input())
