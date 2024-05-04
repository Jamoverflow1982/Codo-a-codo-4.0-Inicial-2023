"""
Crea una función que calcule el Índice de Masa Corporal (IMC) de una
persona.
La función debe recibir dos argumentos: peso (en kilogramos) y altura (en
metros), y retornar el IMC calculado.
Tip: El IMC se calcula dividiendo el peso en kilogramos por el cuadrado de la
altura en metros.
"""

def titulo():
    print('#'*50)
    print(' INDICE MASA CORPORAL '.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def masa(kilo, altura):
    imc=kilo/(altura**2)
    return imc

titulo()
kg=float(input('Ingrese su peso en kilogramos: '))
altura=float(input('Ingrese su altura en metros: '))
print()
print(f' El valor de su IMC es {masa(kg, altura):.2f} '.center(50,'*'))
print()