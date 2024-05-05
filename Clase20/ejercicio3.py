"""
Escribe un programa que tenga un menú que permita elegir si se desea:
1 - Hallar el área de un cuadrado
2 - Hallar el área de un rectángulo
3 - Hallar el área de un triángulo
4 - Hallar el área de un círculo
Cada opción debe hacer uso de una función propia, que pida los datos
necesarios y regrese el valor buscado. El programa principal debe ser el que
imprima el resultado.
"""
def titulo():
    print('-'*50)
    print(' CALCULO DE AREAS '.center(50,'-'))
    print(' by J. Monzon '.rjust(50,'-'))
    print()

def cua_rect(lado1, lado2):
    total=lado1*lado2
    return total

def triangulo(base, altura):
    total=(base*altura)/2
    return total

def circulo(radio):
    total=3.1415926*(radio**2)
    return total

def areas(op):
    print()
    match op:
        case 1:
            print('CALCULO AREA CUADRADO'.center(50,' '))
            print()
            lado1=float(input('Ingrese el primer lado: '))
            lado2=float(input('Ingrese segundo lado: '))
            print(f' El area total es: {cua_rect(lado1, lado2):.2f} '.center(50,'='))
        case 2:
            print('CALCULO AREA RECTANGULO'.center(50,' '))
            print()
            lado1=float(input('Ingrese el primer lado: '))
            lado2=float(input('Ingrese segundo lado: '))
            print(f' El area total es: {cua_rect(lado1, lado2):.2f} '.center(50,'='))
        case 3:
            print('CALCULO AREA TRIANGULO'.center(50,' '))
            print()
            base=float(input('Ingrese tamaño base: '))
            altura=float(input('Ingrese tamaño altura: '))
            print(f' El area total es: {triangulo(base, altura):.2f} '.center(50,'='))
        case 4:
            print('CALCULO AREA CIRCULO'.center(50,' '))
            print()
            radio=float(input('Ingrese tamaño radio: '))
            print(f' El area total es: {circulo(radio):.2f} '.center(50,'='))

titulo()
print(f'1 - Hallar el área de un cuadrado\n2 - Hallar el área de un rectángulo\n3 - Hallar el área de un triángulo\n4 - Hallar el área de un círculo')
print()
op=int(input('Ingrese una opcion: '))
areas(op)
print()