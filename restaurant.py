import numpy
import os
import time
import msvcrt

lista_ruts = []
lista_correo = []
lista_nombre = []
lista_columna = []
lista_filas = []

def fila_columna():
    print("Ver restaurant")
    contador = 1
    for x in range(3):
        print(f"mesa para {(x+1)*2}: " , end=" ")
        for y in range(3):
            print(f"Mesa: {contador}: " reserva_res[x][y], end=" ")
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
        if "@" in correo:
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
    os.system('cls')
    rut = validar_rut()
    nombre = validar_nombre()
    correo = validar_correo()
    personas = validar_personas()
    print("Mesas disponibles:", end=" ")
    contador = 1
    for x in range(3):
        for y in range(3):
            if reserva_res[x][y] == 0:
                if personas <= 2:
                    print(contador)
                elif personas >= 3 and personas <= 3 and x in(1,2):
                    print(contador, end=" ")
                elif personas >= 5 and personas <= 6 and x == 2:
                    print(contador)
            contador+=1
    
    mesa_elegida = validar_mesa()  
    contador = 1

    for x in range(3):
        for y in range(3):
            if contador == mesa_elegida:
                reserva_res[x][y] = 1
                lista_ruts.append(rut)            
                lista_nombre.append(nombre)            
                lista_correo.append(correo)            
                lista_columna.append(y)            
                lista_filas.append(x)            
                

    
    print("Precione una tecla para continuar...")
    msvcrt.getch()


def validar_mesa():
    while True:
        try:
            mesa = int(input("Ingrese una mesa: "))
            if mesa >= 1 and mesa <=9:
                return mesa
            else:
                print("Ingrese una mesa valida!")
        except:
            print("ERROR! ingrese una mesa valida")

















reserva_res = numpy.zeros((3,3), int)


while True:
    os.system('cls')
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
        fila_columna()
    
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