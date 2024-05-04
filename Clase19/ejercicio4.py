"""
Crea una función que calcule el volumen de un cilindro.
La función debe recibir dos argumentos: el radio de la base del cilindro y su
altura.
Tip: El volumen de un cilindro se calcula con la fórmula π * radio^2 * altura.
Para este desafío, puedes usar el valor 3.1415926 como aproximación de π.
"""

def titulo():
    print('='*50)
    print(' VOLUMEN DEL CILINDRO '.center(50,'='))
    print(' by J. Monzon '.rjust(50,'='))
    print()

def volumen(radio, altura):
    total=3.1415926*(radio**2)*altura
    return total

titulo()
radio=float(input('Ingrese el radio del cilindro: '))
altura=float(input('Ingrese la altura: '))
print()
print(f' El volumen total es {volumen(radio, altura):.2f}cm3 '.center(50,'-'))
print()