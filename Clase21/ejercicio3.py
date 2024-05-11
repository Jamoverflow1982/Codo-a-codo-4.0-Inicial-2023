"""
Escribe una función que determine si un número dado es primo o no.
Un número primo es aquel que solo es divisible por sí mismo y por 1,
teniendo exactamente dos divisores distintos.
La función debe recibir un número entero y devolver un valor booleano
indicando si el número es primo.
"""

def titulo():
    print('#'*50)
    print(' NUMEROS PRIMOS '.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def primo(valor):
    divisor=1
    cont=0
    while divisor<=valor:
        total=valor%divisor
        if total==0:
            cont +=1
        divisor +=1
    if cont==2:
        print(f' {valor} ES UN NUMERO PRIMO!!! '.center(50,' '))
        print()
    else:
        print(f' {valor} NO ES UN NUMERO PRIMO!!! '.center(50,' '))
        print()

titulo()
num=int(input('Ingrese un numero para saber si es primo: '))
print()
primo(num)