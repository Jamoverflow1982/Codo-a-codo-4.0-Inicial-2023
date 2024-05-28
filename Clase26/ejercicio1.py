"""
Desafío 1: Programa de Gestión de Listas de Números
Instrucciones:
1. Al iniciar el programa, se mostrará un menú con las opciones disponibles.
2. Selecciona la opción deseada ingresando el número correspondiente.
3. Si eliges la opción para agregar valores, podrás ingresar múltiples números
uno por uno. Para finalizar la carga, ingresa el número 0.
4. Después de agregar valores, puedes seleccionar otras opciones del menú
para realizar operaciones con la lista.
5. Repite las operaciones según sea necesario.
6. Cuando desees salir del programa, elige la opción correspondiente en el
menú.
"""
sistema='clear' #Mac y Linux
#sistema='cls' #Windows
import os
from colorama import Back,Style,Fore,init
init(autoreset=True)

def titulo():
    print(Style.BRIGHT+Back.MAGENTA+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.MAGENTA+Fore.WHITE+'GESTION DE LISTA DE NUMEROS'.center(50,' '))
    print(Style.BRIGHT+Back.MAGENTA+Fore.WHITE+''.center(50,' '))

def menu():
    lista=[]
    while True:
        print()
        print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'MENU'.center(50,' '))
        print('1 - Agregar Valores\n2 - Sumar Valores\n3 - Calcular Promedio\n4 - Mostrar Lista\n5 - Salir\n')
        print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'Ingrese una opcion:', end='')
        op=int(input(' '))
        match op:
            case 1:
                lista=ingreso()
            case 2:
                if lista!=[]:
                    suma(lista)
                else:
                    errorl()
            case 3:
                if lista!=[]:
                    promedio(lista)
                else:
                    errorl()
            case 4:
                if lista!=[]:
                    mostrar(lista)
                else:
                    errorl()
            case 5:
                gracias()
                break
            case _:
                print()
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'A T E N C I O N ! ! !'.center(50,' '))
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'LA OPCION INGRESADA NO ES VALIDA'.center(50,' '))
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'INGRESE UN VALOR ENTRE 1 Y 5'.center(50,' '))
                print()

def ingreso():
    numeros=[]
    print()
    while True:
        val=int(input('Ingrese un numero (o 0 para salir): '))
        if val!=0:
            numeros.append(val)
        else:
            break
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'VALORES ACEPTADOS!!!'.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print()
    return numeros

def mostrar(num):
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'ESTOS SON LOS NUMEROS INGRESADOS:')
    for i in range (len(num)):
        print(num[i], end=' ')
    print('\n')

def suma(num):
    suma=0
    for i in range (len(num)):
        suma=suma+num[i]
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+f'La suma total de la lista es: {suma:.2f}'.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print()

def promedio(num):
    suma=0
    for i in range (len(num)):
        suma=suma+num[i]
    prom=suma/(len(num))
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+f'El promedio de la lista es: {prom:.2f}'.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print()

def errorl():
    print()
    print(Style.BRIGHT+Back.RED+Fore.WHITE+'OPERACION IMPOSIBLE!'.center(50,' '))
    print(Style.BRIGHT+Back.RED+Fore.WHITE+'NO HAY VALORES EN LA LISTA!'.center(50,' '))
    print()

def gracias():
    print()
    print(Style.BRIGHT+Back.LIGHTBLUE_EX+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.LIGHTBLUE_EX+Fore.WHITE+'GRACIAS POR UTILIZAR MI PROGRAMA!!!'.center(50,' '))
    print(Style.BRIGHT+Back.LIGHTBLUE_EX+Fore.WHITE+''.center(50,' '))

os.system(sistema)
titulo()
menu()