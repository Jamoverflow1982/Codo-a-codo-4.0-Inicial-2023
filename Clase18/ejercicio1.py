"""
Desarrollar una función que reciba la longitud de la base y la altura de un
triángulo, y muestre en la pantalla estos dos valores junto al área de la figura.
Tip: el área de cualquier triángulo se calcula multiplicando la longitud de la
base por la altura, y dividiendo el resultado entre dos.
"""

def titulo():
    print('='*50)
    print(' AREA DEL TRIANGULO '.center(50,'='))
    print(' by J. Monzon '.rjust(50,'='))
    print()

def area(base, altura):
    total=(base*altura)/2
    print(f' El area del triangulo es: {total:.2f} '.center(50,'-'))
    print()

titulo()
base=float(input('Ingrese el valor de la base: '))
altura=float(input('Ingrese el valor de la altura: '))
print()
area(base, altura)
