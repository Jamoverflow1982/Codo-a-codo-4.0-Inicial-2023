"""
2- Pedir al usuario que ingrese un número entero. Buscar los números pares menores a él y mostrar la suma de los mismos.
Tener en cuenta:
el uso de contador
el uso de acumulador
Operador módulo/resto:
    numeroUsuario % 2 = 0  es par
    numeroUsuario % 2 = 1  es impar
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)

def gracias():
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(50,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' SUMA NUMEROS PARES '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def pares(num):
    cont=1
    total=0
    while cont<=num:
        res=cont%2
        if res==0:
            print(f'El numero {cont} es par')
            total=total+cont
        cont+=1
    return total

titulo()
numero=int(input('Ingresa un numero para buscar sus pares: '))
print()
totalpar=pares(numero)
print(f'\nLa suma total de los numeros pares es: {totalpar}\n')
gracias()