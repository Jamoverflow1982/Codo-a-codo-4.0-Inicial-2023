"""
Desarrolla una función que calcule el factorial de un número dado.
El factorial de un número n se define como el producto de todos los números
enteros positivos desde 1 hasta n.
Por ejemplo, el factorial de 5 (5!) es 5 x 4 x 3 x 2 x 1 = 120.
La función debe recibir un número entero y devolver su factorial.
"""
def titulo():
    print('#'*50)
    print(' CALCULO FACTORIAL '.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def factorial(valor):
    total=1
    while valor>0:
        total=total*valor
        valor -=1
    print()
    print(f' El valor total del factorial es: {total} '.center(50,'*'))
    print()

titulo()
num=int(input('Ingrese el numero para su factorial: '))
factorial(num)
