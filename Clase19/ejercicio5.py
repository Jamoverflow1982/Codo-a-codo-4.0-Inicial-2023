"""
Crea un programa que permita al usuario realizar operaciones avanzadas con
dos números. Utilizar funciones en cada caso que serán llamadas desde el
programa principal o desde otra función. Las operaciones deben ajustarse a un
menú con estas opciones:
● 1 - Suma.
● 2 - Resta.
● 3 - Multiplicación.
● 4 - División, considerar división por 0.
● 5 - Potencia de los números.
● 6 - Verificar si ambos números son pares.
● 7 - Verificar cuál de los valores es el mayor.
● 8 - Salir.
"""
def titulo():
    print('='*50)
    print(' CALCULADORA '.center(50,'='))
    print(' by J. Monzon '.rjust(50,'='))
    print()

def suma(num1, num2):
    total=num1+num2
    return total

def resta(num1, num2):
    total=num1-num2
    return total

def multi(num1, num2):
    total=num1*num2
    return total

def div(num1, num2):
    total=0
    no=0
    if num2==0:
        no=1
    else:
        total=num1/num2
    return total, no

def pot(num1, num2):
    total=num1**num2
    return total

def par(num1, num2):
    num1p=num1%2
    num2p=num2%2
    if num1p==0 and num2p==0:
        num1=str(num1)
        num2=str(num2)
        res="Los numeros "+num1+" y "+num2+" son pares!!!"
    elif num1p==0:
        num1=str(num1)
        num2=str(num2)
        res="El numero "+num1+" es par y el numero "+num2+" es impar"
    else:
        num1=str(num1)
        num2=str(num2)
        res="El numero "+num2+" es par y el numero "+num1+" es impar"
    return res

def mayor(num1, num2):
    if num1==num2:
        num1=str(num1)
        num2=str(num2)
        res="El "+num1+" y el "+num2+" son iguales"
    elif num1>num2:
        num1=str(num1)
        num2=str(num2)
        res="El "+num1+" es mayor que el numero "+num2
    else:
        num1=str(num1)
        num2=str(num2)
        res="El "+num2+" es mayor que el numero "+num1
    return res

def opcion(num):
    match num:
        case 1:
            print(f'La suma total entre {num1} y {num2} es {suma(num1, num2)}'.center(50,' '))
        case 2:
            print(f'La resta entre {num1} y {num2} es {resta(num1, num2)}'.center(50,' '))
        case 3:
            print(f'La multiplicacion entre {num1} y {num2} es {multi(num1, num2)}'.center(50,' '))
        case 4:
            totaldiv, no=div(num1, num2)
            if no==1:
                print(f' El divisor no puede ser {num2} '.center(50,'*'))
                print(' OPERACION IMPOSIBLE '.center(50,'*'))
            else:
                print(f'La division entre {num1} y {num2} es {totaldiv:.0f}'.center(50,' '))
        case 5:
            print(f'El numero {num1} elevado a {num2} es {pot(num1, num2)}'.center(50,' '))
        case 6:
            print(par(num1, num2).center(50,' '))
        case 7:
            print(mayor(num1, num2).center(50,' '))
        case 8:
            print('GRACIAS POR USAR MI PROGRAMA!!!'.center(50,' '))
        case _:
            print(f'{num} NO ES UNA OPCION VALIDA'.center(50,' '))

titulo()
print('Ingrese operacion a realizar:\n1 - Suma\n2 - Resta\n3 - Multiplicación\n4 - División\n5 - Potencia\n6 - Verificar si ambos números son pares\n7 - Verificar cuál de los valores es el mayor\n8 - Salir')
print()
op=int(input('Opcion?: '))
if op>=8:
    print()
    print('-'*50)
    opcion(op)
else:
    num1=int(input('Ingrese el primer numero: '))
    num2=int(input('Ingrese el segundo numero: '))
    print()
    print('-'*50)
    opcion(op)
print('-'*50)
print()
