"""
Escribe una función que convierta temperaturas de Celsius a Fahrenheit y
viceversa.
La función debe recibir dos argumentos: el valor de la temperatura y la
unidad de origen ('C' para Celsius, 'F' para Fahrenheit).
Debe retornar la temperatura convertida a la unidad opuesta.
Tip: para convertir Celsius a Fahrenheit la fórmula es (Celsius * 9/5) + 32, y para
convertir Fahrenheit a Celsius es (Fahrenheit - 32) * 5/9.
"""

def titulo():
    print('-'*60)
    print(' CONVERTIDOR DE GRADOS '.center(60,'-'))
    print(' by J. Monzon '.rjust(60,'-'))
    print()

def covertir(valor, unidad):
    unidad=unidad[0].upper()
    if unidad=="C":
        unidadC="F"
        valor=(valor*(9/5))+32
    elif unidad=="F":
        unidadC="C"
        valor=(valor-32)*(5/9)
    else:
        unidadC="E"
    return valor, unidad, unidadC

def resultado(valor, dato, unidad):
    if unidad=="E":
        print()
        print(f'La unidad {dato} no es valida!!!'.center(60,' '))
        print('debe ingresar C o F'.center(60,' '))
        print()
    else:
        print()
        print('*'*60)
        print(f' La conversion es {valor:.2f}{unidad}° '.center(60,'*'))
        print('*'*60)
        print()

titulo()
valor=float(input('Ingrese el valor de la temperatura: '))
unidad=input('Ingrese la unidad (C = Celsius o F = Fahrenheit): ')
valorF, dato, unidadF=covertir(valor, unidad)
resultado(valorF, dato, unidadF)