"""
Escribir un programa que permita obtener la tabla de multiplicar de un valor
ingresado por el usuario.
"""

def titulo():
    print('#'*50)
    print(' TABLA DE MULTIPLICAR '.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def tabla(valor):
    while valor>=0:
        multi=0
        while multi<=10:
            if multi==0:
                print()
                print(f' LA TABLA DEL {valor} ES: '.center(50,' '))
                print()
            print(f'{valor} X {multi} = {valor*multi}'.center(50,' '))
            multi +=1
        valor -=1        
    print()

titulo()
num=int(input('Ingrese el valor a multiplicar: '))
tabla(num)