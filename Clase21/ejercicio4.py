"""
Implementa una función que genere una lista conteniendo los primeros n
números de la secuencia Fibonacci.
En la secuencia Fibonacci, cada número es la suma de los dos anteriores,
siendo los dos primeros números 0 y 1. La función debe recibir un número
entero n y retornar una lista con la secuencia.
"""

def titulo():
    print('+'*80)
    print(' SECUENCIA FIBONACCI '.center(80,'+'))
    print(' by J. Monzon '.rjust(80,'+'))
    print()

def fibonacci(valor):
    print()
    print('-'*80)
    print('La secuencia Fibonacci es: ',end='')
    contador=0
    num1=0
    num2=0
    while contador<valor:
        if num2==0:
            print(f'{num2}',end=' ')
            num2 +=1
            print(f'{num2}',end=' ')
            contador +=2
        else:
            total=num1+num2
            print(f'{total}',end=' ')
            num1=num2
            num2=total
            contador +=1
    print()
    print('-'*80)
    print('\n')

titulo()
num=int(input('Ingrese un numero cantidad de numeros: '))
fibonacci(num)