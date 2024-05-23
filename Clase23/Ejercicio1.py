"""
Desafío 1: Suma de Números Naturales
Desarrolla una función que calcule la suma de los números naturales hasta un
número dado utilizando un bucle for. La suma de los números naturales hasta
el número n se define como la suma de todos los números enteros positivos
desde 1 hasta n.
"""
from colorama import Back,Fore,Style,init
init(autoreset=True)

def titulo():
    print('*'*50)
    print(' SUMA DE NUMEROS NATURALES '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def suma(num):
    cont2=0
    for cont in range (1, num+1):
        cont2=cont2+cont
    return cont2

titulo()
while True:
    valor=int(input('Ingrese el numero final natural: '))
    if valor>=1:
        res=suma(valor)
        print()
        print(Style.BRIGHT+Fore.WHITE+Back.GREEN+f'El valor final de la suma es: {res}'.center(50,' '))
        print()
        break
    else:
        print()
        print(Style.BRIGHT+Back.RED+Fore.WHITE+'Ingrese un numero mayor a cero'.center(50,' '))
        print(Style.BRIGHT+Back.RED+Fore.WHITE+'VUELVA A INTENTARLO'.center(50,' '))
        print()