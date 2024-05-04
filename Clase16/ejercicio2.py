"""
Escribe un programa en Python que solicite al usuario ingresar el código de
un producto y determine a qué categoría pertenece según las siguientes
reglas:
Si el código comienza con "A", el producto es de tipo "Electrónico".
Si el código comienza con "B", el producto es de tipo "Ropa".
Si el código comienza con "C", el producto es de tipo "Alimenticio".
Si el código no coincide con ninguna de las anteriores, el programa debe
mostrar un mensaje indicando que el tipo de producto es
"Desconocido".
Importante: No utilizar condicionales anidados para resolver este ejercicio.
"""

def titulo():
    print('*'*50)
    print(' CATEGORIA DE PRODUCTOS '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def categoria(prod):
    prod1=prod[0].upper()
    print('*'*50)
    match prod1:
        case "A":
            print(f' El producto {prod} es de tipo "Electrónico" '.center(50,'*'))
        case "B":
            print(f' El producto {prod} es de tipo "Ropa" '.center(50,'*'))
        case "C":
            print(f' El producto {prod} es de tipo "Alimenticio" '.center(50,'*'))
        case "D":
            print(f' El producto {prod} es de tipo "Alimenticio" '.center(50,'*'))
        case _:
            print(f' {prod} ES UN PRODUCTO DESCONOCIDO '.center(50,'*'))
    print('*'*50)

titulo()
prod=input('Ingrese el codido del articulo: ')
print()
categoria(prod)
print()