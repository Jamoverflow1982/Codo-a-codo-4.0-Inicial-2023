"""
Desafío 2: Tabla de multiplicar
Escribir un programa que permita obtener la tabla de multiplicar de un valor
ingresado por el usuario.
"""

from colorama import Back,Fore,Style,init
init(autoreset=True)

def titulo():
    print('*'*50)
    print(' TABLA DE MULTIPLICAR '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def validar():
    while True:
        numero=int(input('Ingrese el numero a multiplicar (entre 0 y 10): '))
        if numero<0 or numero>10:
            print()
            print(Style.BRIGHT+Back.RED+Fore.WHITE+f'EL {numero} NO ESTA ENTRE 0 Y 10'.center(50,' '))
            print(Style.BRIGHT+Back.RED+Fore.WHITE+'INGRESE EL NUMERO NUEVAMENTE'.center(50,' '))
            print()
        else:
            break
    return numero

def multiplicar(num):
    print()
    for numm in range (num+1):
        print(Style.BRIGHT+Back.RED+Fore.WHITE+f'TABLA DEL {numm}'.center(50,' '))
        for multi in range (1,11):
            print(Style.BRIGHT+Back.BLUE+Fore.WHITE+f'{numm} X {multi} = {numm*multi}'.center(50,' '))
    print()

titulo()
multiplicar(validar())