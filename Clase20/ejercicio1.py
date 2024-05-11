"""
Crea un programa que pida al usuario un número entero que representa a
un año, y que use una función para determinar si ese año es bisiesto o no.
La función debe retornar un valor booleano indicando si el año es bisiesto.
Recuerda: Un año es bisiesto si es divisible por 4, excepto aquellos años que
son divisibles por 100, a menos que también sean divisibles por 400.
"""

def titulo():
    print('*'*50)
    print(' CALCULADORA AÑO BISIESTO '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def bisiesto(anio):
    val1=anio%100
    val2=anio%4
    val3=anio%400
    if val1==0 and val2==0 and val3==0:
        res=True
    elif val2==0 and not val1==0:
        res=True
    else:
        res=False
    return res

titulo()
anio=int(input('Ingrese año:'))
print(f'Bisiesto: {bisiesto(anio)}')
print()
