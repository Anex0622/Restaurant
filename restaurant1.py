import numpy
import os
import time
import msvcrt


def fila_columna():
    for x in range(3):
        print(f"Fila {x+1}:\t" , end="")
        for y in range(3):
            print(reserva_res[x][y], end=" ")
    print()
        
    print("        1 2 3")
    
    
    
    print("\nPresione una tecla para continuar...")
    msvcrt.getch()

def validar_personas():
    while True:
        try:
            personas = int(input("Ingrese cantidad de personas(limite de 6):"))
            if personas >= 1 and personas <= 6:
                return personas
            else:
                print("ERROR! ingrese un maximo de 6 personas")
        except:
            print("ERROR! ingrese un numero entero")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_fila_():
    while True:
        try:
            fila = int(input("Ingrese mesa que desea comprar(2,4 o 6):"))
            if fila >= 1 and fila <= 3:
                break
            else:
                print("ERROR! ingrese un numero de una de las mesas")
        except:
            print("ERROR! ingrese un numero entero")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese la columna que desea comprar(1,2 o 3): "))
            if columna >= 1 and columna <= 3:
                return columna
            else:
                print("ERROR! Ingrese una de las columnas")
        except:
            print("ERROR! Ingrese un numero entero!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if len(str(rut)) == 8:
                return rut
            else:
                print("Ingrese un rut valido porfavor")
        except:
            print("Ingrese un rut valido porfavor")

def validar_correo():
    while True:
        correo = input("Ingrese su correo: ")
        if correo in "@":
            return correo
        else:
            print("Ingrese un correo valido!")

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3:
            return nombre
        else:
            print("Ingrese un nombre valido de mas de 3 letras") 

def reserva():
    rut = validar_rut()
    nombre = validar_nombre()
    correo = validar_correo()
    personas = validar_personas()
















reserva_res = numpy.zeros((3,3), int)


while True:
    print("""Menú
    1.	Ver restaurant
    2.	Reservar mesa
    3.	Carta
    4.	Pagar
    5.	Cancelar
    6.	Salir""")
    opcion = validar_opcion()
    if opcion == 1:
        print("             Ver el restaurant          ")
        print("fila 1       |()| |()| |()|             ")
        print("               _     _     _            ")
        print("fila 2       |( )| |( )| |( )|          ")
        print("               -     -     -            ")
        print("              _  _   _  _   _  _        ")
        print("fila 3       |(  )| |(  )| |(  )|       ")
        print("              -  -   -  -   -  -        ")
        for x in range(3):
            print(f"Fila {x+1}:\t" , end="")
            for y in range(3):
                print(reserva_res[x][y], end=" ")
            print()
        print("        1 2 3")
        
        
        print("\nPresione una tecla para continuar...")
        msvcrt.getch()
    
    elif opcion == 2:
        reserva()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        break