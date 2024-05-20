"""
1- Se necesita calcular el promedio de ciertos valores. Pide al usuario que ingrese la cantidad de valores que quiere promediar. Luego el usuario debe ingresar esos valores.

El programa calculará el promedio de los valores ingresados y mostrará el resultado.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)

def gracias():
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(80,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(80,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print(' PROMEDIO '.center(80,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print()

def promedio(num):
    cont=0
    total=0
    while cont<num:
        val=float(input(Fore.LIGHTBLUE_EX+f'Ingrese el numero {cont+1}: '))
        total=total+val
        cont+=1
    res=total/num
    return res

titulo()
num=int(input(Style.BRIGHT+Fore.LIGHTBLUE_EX+'Ingrese la cantidad de numeros a promediar: '))
print()
total=promedio(num)
print(Style.BRIGHT+Fore.YELLOW+f'\nEl promedio total de los numeros ingresados es: {total:.2f}\n')
gracias()