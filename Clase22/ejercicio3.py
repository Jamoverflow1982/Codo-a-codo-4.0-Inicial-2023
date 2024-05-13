"""
Desafío 3: Sumador de números pares e impares
Desarrolla un programa que permita ingresar números positivos hasta que se
ingrese 0. Al finalizar se deberá mostrar:
● La suma de los números pares.
● El promedio de los números impares.
● La cantidad de números ingresados.
● El número par más alto.
● El número impar más bajo.
"""
from colorama import Fore, init
init(autoreset=True)

def titulo():
    print(Fore.CYAN+'#'*50)
    print(' SUMA DE NUMEROS PARES E IMPARES '.center(50,'#'))
    print(Fore.CYAN+' by J. Monzon '.rjust(50,'#'))
    print()

def validar(valor):
    continuar=0
    if valor>=0:
        pase=valor
    else:
        if valor!=0:
            while continuar==0:
                print('-'*50)
                print(Fore.RED+'El numero tiene que ser un numero positivo'.center(50,' '))
                print(Fore.RED+'VUELVA A INGRESAR EL NUMERO O CERO PARA SALIR'.center(50,' '))
                print('-'*50)
                valor=float(input('Ingrese un numero (ingrese 0 para salir): '))
                if valor>=0:
                    pase=valor
                    continuar=1
    return valor

def suma(valor):
    totalpares=0
    totalimpares=0
    impares=0
    cantidad=0
    cantpares=0
    paralto=0
    imparbajo=1000
    promnumimp=0
    while valor>0:
        cantidad +=1
        par=valor%2
        if par==0:
            totalpares=totalpares+valor
            cantpares +=1
            if paralto<valor:
                paralto=valor
        else:
            impares +=1
            totalimpares=totalimpares+valor
            if imparbajo>valor:
                imparbajo=valor
        num=float(input('Ingrese un numero (ingrese 0 para salir): '))
        valor=validar(num)
    if impares!=0 and totalimpares!=0:
        promnumimp=totalimpares/impares
    else:
        imparbajo=0
    return totalpares, promnumimp, cantidad, paralto, imparbajo

titulo()
num=float(input('Ingrese un numero (ingrese 0 para salir): '))
pares, promim, cant, paral, impba = suma(validar(num))
if cant>0:
    print()
    print(Fore.GREEN+'#'*50)
    print(f'Cantidad de numeros ingresados\t{cant}\nTotal suma pares\t\t{pares:.0f}\nPromedio impares\t\t{promim:.2f}\nNumero par mas alto\t\t{paral:.0f}\nNumero impar mas bajo\t\t{impba:.2f}')
    print(Fore.GREEN+'#'*50)
    print()
else:
    print(Fore.RED+'*'*50)
    print(Fore.RED+'NO SE INGRESO NINGUN NUMERO!!!')
    print(Fore.RED+'*'*50)