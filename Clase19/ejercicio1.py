"""
Escribe una función en Python que convierta kilómetros a millas.
La función debe recibir como argumento el número de kilómetros y retornar
el equivalente en millas.
"""

def titulo():
    print('='*60)
    print(' KILOMETROS A MILLAS '.center(60,'='))
    print(' by J. Monzon '.rjust(60,'='))
    print()

def convertir (km):
    millas=km*1.60934
    return millas

titulo()
km=float(input('Ingresar kilometros: '))
print()
print(f'El equivalente de {km:.2f} kilometros es {convertir(km):.2f} millas'.center(50,'*'))
print()