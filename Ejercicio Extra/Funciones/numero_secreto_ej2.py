"""
2. ¡Adivina un número! Crea un programa permita al usuario adivinar un número secreto, que tendrás guardado en una variable. Cuando el usuario arriesgue un valor el programa le informará si el número ingresado es mayor o menor que el número secreto, y si es igual adivinó!. Se ejecutará hasta que el usuario quiera salir, y se informará antes de finalizar, cuántos intentos fueron necesarios para adivinar el número secreto.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)
num=23

def gracias():
    print()
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(50,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' ADIVINA EL NUMERO '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def adivina(num):
    cont=0
    acierto=0
    while acierto!=num:
        cont+=1
        acierto=int(input('Ingrese un numero: '))
        print()
        if acierto>num:
            print(f'El numero {acierto} es mayor al numero guardado')
            print('INTENTA DENUEVO!!!')
        elif acierto<num:
            print(f'El numero {acierto} es menor al numero guardado')
            print('INTENTA DENUEVO!!!')
        print()
    print(Style.BRIGHT+Back.CYAN+Fore.WHITE+f'ADIVINASTE!!! Es el numero {num}!!!'.center(50,' '))
    print(Style.BRIGHT+Back.CYAN+Fore.WHITE+f'Te llevo {cont} intentos conseguirlo!!!'.center(50,' '))

titulo()
adivina(num)
gracias()