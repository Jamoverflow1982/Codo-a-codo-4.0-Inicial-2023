"""
Desarrolla un programa que permita mostrar los siguientes patrones. Luego
crear una función para cada uno utilizando For y un menú que permita
seleccionar cuál imprimir.
"""

from colorama import Style,Back,Fore,init
init(autoreset=True)

def formas(num):
    match num:
        case 1:
            print()
            for ast in range(-1,10,2):
                cara='*'*ast
                print(cara.center(50,' '))
            print()
        case 2:
            print()
            for fila in range (1,5):
                for columna in range(1,9):
                    print('*',end=' ')
                print()
            print()
        case 3:
            print()
            for ast in range(-1,10,2):
                cara='*'*ast
                print(cara.center(50,' '))
            for ast in range(7,0,-2):
                cara='*'*ast
                print(cara.center(50,' '))
            print()
        case 4:
            for fila in range (0,7):
                print()
                print(' '*fila,end='')
                for columna in range (1,11):
                    print('*',end='')
            for fila in range (5,-1,-1):
                print()
                print(' '*fila,end='')
                for columna in range (1,11):
                    print('*',end='')
            print('\n\n')

def figuras():
    print('SELECCIONE LA FORMA A VISUALIZAR')
    print('1 - Triangulo escaleno\n2 - Rectangulo de 8 x 4\n3 - Rombo\n4 - Flecha\n')
    while True:
        forma=int(input('Ingrese su eleccion: '))
        if forma<=4 or forma>=1:
            break
        else:
            print(Style.BRIGHT+Back.RED+Fore.WHITE+'INGRESE UN VALOR VALIDO ENTRE 1 Y 4')
    return forma

formas(figuras())