import re
import json


def regex_1():
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


def regex_2():
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


def intercambio_1():
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
            print(
                f"Cantidad de sensores de la estación “{estacion['nombre']}”: {len(estacion['sensores'])}")
            for sensor in estacion['sensores']:
                print(
                    f"{sensor['nombre']}: {sensor['medicion']}{sensor['unidad']}")
            print('')
            return
        print('---------------')
    print('')
    print("No se ha encontrado la estacion con el nombre seleccionado")
    print('')


def intercambio_2():
    archivo = open('estaciones.json',)
    estaciones = json.load(archivo)
    ordenadas = sorted(estaciones, key=lambda estacion: sum(
        estacion['bateria']) / len(estacion['bateria']))
    print('')
    print(f"La estacion con menos bateria es: {ordenadas[0]['nombre']}")
    print('')
    archivo.close()


def recursividad_1():
    def convertir(numero):
        if len(numero) == 1:
            return numero
        else:
            if (int(numero[0]) % 2 == 0):
                return "1" + convertir(numero[1:])
            else:
                return "2" + convertir(numero[1:])

    print("--------------")
    numero = str(input("Ingrese el nombre a convertir: "))
    print("--------------")
    print("Resultado: ", convertir(numero))
    print("--------------")


def recursividad_2():
    def unificar(listas):
        if len(listas) == 1:
            return listas[0]
        else:
            return listas[0] + unificar(listas[1:])

    listas = [[1, 2, 3], [4, 5, 6], [7], [8]]
    print("--------------")
    print("Resultado: ", unificar(listas))
    print("--------------")


def recursividad_3():
    def decidir(lista1, lista2):
        if len(lista1) == 0 and len(lista2) == 0:
            return True
        elif lista1[0] == lista2[0]:
            return decidir(lista1[1:], lista2[1:])
        return False

    lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lista2 = [7, 6, 3, 4, 5, 2, 8, 1]
    print("--------------")
    print("Resultado: ", decidir(lista1, lista2))
    print("Resultado: ", decidir(lista1, lista1))
    print("--------------")


def mostrar_menu():
    print("")
    print("Elija el ejercicio que quiere ejecutar")
    print("1 - Expresiones regulares, ejercicio 1: Validacion de codigo de aerolineas")
    print("2 - Expresiones regulares, ejercicio 2: Validacion de numero menor a 1900")
    print("3 - Formatos de intercambio de datos, ejercicio 1: Obtener informacion de estacion")
    print("4 - Formatos de intercambio de datos, ejercicio 2: Calcular estacion con menos bateria")
    print("5 - Recursion, ejercicio 1: Convertir digitos pares/impares")
    print("6 - Recursion, ejercicio 2: Unificar lista de listas")
    print("7 - Recursion, ejercicio 3: Listas son iguales?")
    print("0 - Salir")


mostrar_menu()
eleccion = int(input())

while eleccion != 0:
    if eleccion == 1:
        regex_1()
    if eleccion == 2:
        regex_2()
    if eleccion == 3:
        intercambio_1()
    if eleccion == 4:
        intercambio_2()
    if eleccion == 5:
        recursividad_1()
    if eleccion == 6:
        recursividad_2()
    if eleccion == 7:
        recursividad_3()
    mostrar_menu()
    eleccion = int(input())
