"""
Desafío 1: Patrones visuales
Desarrolla un programa que permita mostrar los siguientes patrones. Luego
crear una función para cada uno y un menú que permita seleccionar cuál
imprimir.
"""

def titulo():
    print('*'*50)
    print(' PATRONES VISUALES '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def triangulo():
    fila=1
    columna=4
    while fila<=9:
        print(' '*(columna),'*'*(fila))
        fila +=2
        columna -=1

def rectangulo():
    fila=1
    while fila<=4:
        print(' * '*8)
        fila +=1

def rombo():
    fila=1
    columna=4
    while fila<=9:
        print(' '*(columna),'*'*(fila))
        fila +=2
        columna -=1
    fila -=4
    columna +=2
    while fila>=1:
        print(' '*(columna),'*'*(fila))
        fila -=2
        columna +=1

def flecha():
    columna=1
    while columna<=7:
        columna +=1
        print(' '*(columna),'*'*10)
    while columna>1:
        columna -=1
        print(' '*(columna),'*'*10)

titulo()
ingreso=0
while ingreso==0:
    print('1 - Triangulo Escaleno\n2 - Rectangulo\n3 - Rombo\n4 - Flecha')
    op=int(input('Elija una figura: '))
    print()
    match (op):
        case 1: 
            triangulo()
            ingreso=1
        case 2: 
            rectangulo()
            ingreso=1
        case 3: 
            rombo()
            ingreso=1
        case 4: 
            flecha()
            ingreso=1
        case _:
            print('-'*50)
            print(f'EL VALOR {op} NO CORRESPONDE A UNA OPCION!'.center(50,' '))
            print('INTENTE NUEVAMENTE'.center(50,' '))
            print('-'*50)
print()