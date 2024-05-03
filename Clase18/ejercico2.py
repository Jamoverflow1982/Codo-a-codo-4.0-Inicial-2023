"""
Desarrollar una función que reciba un número entero de 0 a 10, y que muestre
por la terminal la tabla de multiplicar por ese número.
Algunas ideas que puedes implementar:
●
●
Verificar que el valor recibido está en el rango correcto.
Poner un título antes de comenzar a mostrar la tabla solicitada.
"""

def titulo():
    print('='*50)
    print(' TABLA DE MULTIPLICAR '.center(50,'='))
    print(' by J. Monzon '.rjust(50,'='))
    print()

def multiplicador(num):
    print()
    print('-'*50)
    print(f'{num} X 0 = {num*0}\n{num} X 1 = {num*1}\n{num} X 2 = {num*2}\n{num} X 3 = {num*3}\n{num} X 4 = {num*4}\n{num} X 5 = {num*5}\n{num} X 6 = {num*6}\n{num} X 7 = {num*7}\n{num} X 8 = {num*8}\n{num} X 9 = {num*9}\n{num} X 10 = {num*10}')
    print('-'*50)

def error(num):
    print()
    print('*'*50)
    print(f' EL NUMERO {num} NO ESTA ENTRE 0 Y 10 '.center(50,'*'))
    print('*'*50)

titulo()
num=int(input('Ingrese un numero entre el 0 al 10: '))
if num>=0 and num<=10:
    multiplicador(num)
else:
    error(num)