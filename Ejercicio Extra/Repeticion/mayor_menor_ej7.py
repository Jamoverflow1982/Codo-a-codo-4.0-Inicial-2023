"""
7- Se ingresan números hasta que se introduce un cero. La computadora muestra el máximo y el mínimo.
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
    print(' MAYOR Y MENOR '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def ingreso():
    num=-100000
    mayor=0
    menor=100000
    while num!=0:
        if num==-100000:
            num=int(input('Ingrese un numero o 0 para salir: '))
        else:
            num=int(input('Ingrese otro numero o 0 para salir: '))
        if num!=0:
            if num>=mayor:
                mayor=num
            if num<=menor:
                menor=num
    return mayor, menor

titulo()
may,men=ingreso()
print()
print(Style.BRIGHT+Fore.RED+Back.LIGHTWHITE_EX+'RESULTADO FINAL'.center(50,' '))
print(Style.BRIGHT+Fore.LIGHTGREEN_EX+Back.LIGHTWHITE_EX+f'EL MAYOR ES {may}'.center(50,' '))
print(Style.BRIGHT+Fore.LIGHTGREEN_EX+Back.LIGHTWHITE_EX+f'EL MENOR ES {men}'.center(50,' '))
print()
gracias()