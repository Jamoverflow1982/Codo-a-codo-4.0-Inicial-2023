"""
5- Se ingresan 5 números. La computadora muestra los números ingresados, cuál fue el mayor y en qué orden apareció. 
Ejemplo: Se ingresa 4 8 6 7 5, la computadora muestra “El mayor es 8, en la 2º posición”.
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
    print(' NUMERO Y POSICION MAYOR '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def mayor():
    pos=0
    num=0
    cont=0
    while cont<5:
        cont+=1
        num_ing=int(input(f'Ingrese el {cont}º numero: '))
        if num_ing>=num:
            num=num_ing
            pos=cont
    return num, pos

titulo()
num_mayor, pos_mayor=mayor()
print()
print(Style.BRIGHT+Fore.CYAN+f'El mayor es {num_mayor}, en la {pos_mayor}º posición'.center(50,' '))
gracias()