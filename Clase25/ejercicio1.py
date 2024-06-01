"""
Desafío 1: Creación de un Ticket de Compra
Desarrollar un programa que permita al usuario generar un ticket de compra
ingresando productos y sus respectivos precios en dos listas distintas. El ingreso
de datos se realiza mediante un bucle while, donde el usuario tiene la opción de
agregar más productos o finalizar la entrada de datos. Una vez que se
completan las entradas y se sale del bucle, el programa muestra el ticket de
compra, que incluye el nombre y el precio de cada producto, así como el total a
pagar. Para asegurar una presentación ordenada, cada producto se alinea a la
izquierda y su precio a la derecha en el ticket, utilizando los métodos ljust() y
rjust(). El total a pagar también se alinea a la derecha para mantener la
consistencia visual con los precios de los productos.
"""

from colorama import Style,Back,Fore,init
init(autoreset=True)

productos=[]
val_productos=[]

def titulo():
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'TICKET DE COMPRA'.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print()

def gracias():
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'GRACIAS POR UTILIZAR MI PROGRAMA'.center(50,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+''.center(50,' '))
    print()

def ingreso(productos, val_productos):
    while True:
        pro=input('\nIngrese el nombre del producto: ')
        productos.append(pro)
        val=float(input('Ingrese el valor del producto: $'))
        val_productos.append(val)
        print()
        print(Fore.WHITE+Back.CYAN+'Desea continuar ingresando productos?')
        salir=input('Presione ENTER continuar o S para salir:')
        salir=salir.upper()
        if salir=='S':
            break
    return productos, val_productos

def listado(productos, precios):
    suma=0
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'TICKET DE COMPRA'.center(50,' '))
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'Producto'.ljust(25,' '), end='')
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'Precio'.rjust(25,' '))
    for producto, precio in zip(productos, precios):
        print(f'{producto}'.ljust(25,' ').capitalize(), end='')
        print(f'${precio:.2f}'.rjust(25,' '))
        suma=suma+precio
    print()
    print(Style.BRIGHT+Back.RED+Fore.WHITE+f'TOTAL ${suma:.2f}'.rjust(50,' '))

titulo()
ingreso(productos, val_productos)
listado(productos, val_productos)
gracias()