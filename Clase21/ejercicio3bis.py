"""
Escribe una función que determine si un número dado es primo o no.
Un número primo es aquel que solo es divisible por sí mismo y por 1,
teniendo exactamente dos divisores distintos.
La función debe recibir un número entero y devolver un valor booleano
indicando si el número es primo.
Desafío extra:
¿Te animas a escribir un programa que
muestre la cantidad de números primos que
existen entre 2 y un número entero
cualquiera ingresado por el usuario?
"""

def titulo():
    print('#'*50)
    print(' NUMEROS PRIMOS DESDE 2 AL ELEGIDO'.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def primo(valor):
    print('LOS NUMEROS PRIMOS SON:')
    while valor>=2:
        divisor=1
        cont=0
        while divisor<=valor:
            total=valor%divisor
            if total==0:
                cont +=1
            divisor +=1
        if cont==2:
            print(valor, end='\n')
        valor -=1

titulo()
num=int(input('Ingrese un numero para saber si es primo: '))
print()
primo(num)
print()
print()