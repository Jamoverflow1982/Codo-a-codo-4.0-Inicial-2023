"""
4- Dado un entero N entre 1 y 10 (inclusive), la computadora muestra la tabla de multiplicar de N.
"""
from colorama import Fore, Back, Style, init
init(autoreset=True)

def gracias():
    print()
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(50,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' TABLA DE MULTIPLICAR '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def tabla (num):
    cont=0
    while cont<=10:
        print(f'{num} X {cont} = {num*cont}')
        cont+=1

def validar():
    valido=False
    while valido!=True:
        num=int(input('Ingrese un numero ente 1 y 10: '))
        if num>=1 and num<=10:
            valido=True
        else:
            print()
            print(Style.BRIGHT+Fore.LIGHTRED_EX+'*'*80)
            print(Style.BRIGHT+Fore.LIGHTRED_EX+f' {num} NO ES UN VALOR ENTRE 1 Y 10 '.center(80,'*'))
            print(Style.BRIGHT+Fore.LIGHTRED_EX+' INGRESE UN NUMERO VALIDO '.center(80,'*'))
            print(Style.BRIGHT+Fore.LIGHTRED_EX+'*'*80)
            print()
    print()
    return num

titulo()
tabla(validar())
gracias()