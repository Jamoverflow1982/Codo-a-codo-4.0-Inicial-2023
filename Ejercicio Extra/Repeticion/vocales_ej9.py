"""
9- Desarrollar un programa que pida al usuario ingresar una letra y que por cada carga pregunte “¿Desea ingresar otra letra? [S/N]”. La carga de datos finaliza cuando se ingresa una n o N. La computadora debe mostrar la cantidad de letras vocales ingresadas.
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
    print(' CONTADOR DE VOCALES '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def vocales():
    salir='S'
    cont=0
    while salir!='N':
        letra=input('Ingrese una letra: ')
        letra=letra.upper()
        if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
            cont+=1
        salir=input('¿Desea ingresar otra letra? [S/N]: ')
        salir=salir.upper()
    return cont

titulo()
cont=vocales()
print()
print(Style.BRIGHT+Back.CYAN+Fore.LIGHTWHITE_EX+f'La cantidad de vocales ingresadas es: {cont}'.center(50,' '))
gracias()