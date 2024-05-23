"""
Desafío 3: Múltiplos de un número
Escribir un programa que muestre todos los múltiplos de un número dado
dentro de un rango definido por otro número. El programa debe solicitar al
usuario ingresar dos números enteros: el número base del cual se calcularán
los múltiplos y el límite superior del rango. Luego imprimirá todos los
múltiplos del número base que estén dentro del rango especificado,
incluyendo el límite superior.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)
import os

def titulo():
    print(Fore.CYAN+'#'*50)
    print(' MULTIPLOS DE UN NUMERO '.center(50,'#'))
    print(Fore.CYAN+' by J. Monzon '.rjust(50,'#'))
    print()

def multiplos(rango, base):
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+f'Los multiplos de {base} dentro del rango: {rango}'.center(50,' '))
    for cont in range (base, rango, base):
        print(Style.BRIGHT+Back.GREEN+Fore.WHITE+f'{cont}',end=Style.BRIGHT+Back.GREEN+Fore.WHITE+' ')
    print('\n')

titulo()
base=int(input('Ingrese el numero base: '))
rango=int(input('Ingrese el limite superior del rango: '))
multiplos(rango,base)