"""
Desafío 2: Secuencia numérica
Desarrolla un programa que permita crear una secuencia numérica. El usuario
ingresará tres valores: inicio, fin y salto. Utilizar While para validar lo siguiente:
● El valor de inicio debe ser un número positivo.
● El valor de fin debe ser mayor que el de inicio.
● El valor de salto no puede ser cero o negativo.
"""
iniciar=0
iniciar2=0
iniciar3=0

def titulo():
    print('#'*50)
    print(' SECUENCIA NUMERICA '.center(50,'#'))
    print(' by J. Monzon '.rjust(50,'#'))
    print()

def secuencia(valor1, valor2, valor3):
    while valor1<=valor2:
        print((valor1),end=' ')
        valor1=valor1+valor3
    print()

titulo()
while iniciar==0:
    num1=int(input('Ingrese el numero de inicio: '))
    if num1>0:
        iniciar=1
        while iniciar2==0:
            num2=int(input('Ingrese el numero de fin: '))
            if num2>num1:
                iniciar2=1
                while iniciar3==0:
                    num3=int(input('Ingrese el numero de salto: '))
                    if num3>0 and num3<num2:
                        iniciar3=1
                        print()
                        print('*'*50)
                        print('La secuencia numerica es:')
                        secuencia(num1, num2, num3)
                        print('*'*50)
                        print()
                    else:
                        print('-'*50)
                        print('El valor de salto tiene que ser un numero positivo'.center(50,' '))
                        print('VUELVA A INGRESAR EL NUMERO DE SALTO Y MENOR AL DE FIN'.center(50,' '))
                        print('-'*50)
            else:
                print('-'*50)
                print('El valor fin tiene que ser mayor al numero inicio'.center(50,' '))
                print('VUELVA A INGRESAR EL NUMERO FINAL'.center(50,' '))
                print('-'*50)
    else:
        print('-'*50)
        print('El valor de inicio tiene que ser un numero positivo'.center(50,' '))
        print('VUELVA A INGRESAR EL NUMERO INICIAL'.center(50,' '))
        print('-'*50)