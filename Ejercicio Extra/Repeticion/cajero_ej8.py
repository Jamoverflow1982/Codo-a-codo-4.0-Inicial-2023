"""
8- Una cuenta bancaria tiene 30000 pesos de saldo. El usuario ingresará valores que corresponden a extracciones vía cajero automático. Por cada extracción se debe mostrar cómo quedó el saldo luego de la operación. Una extracción que supere al saldo disponible se debe rechazar indicando que no es posible la operación. El programa finaliza cuando el saldo queda en cero.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)

def gracias():
    print()
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(50,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print(' CAJERO AUTOMATICO '.center(50,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*50)
    print()

def cajero():
    saldo=30000
    while saldo>0:
        print(f'Saldo disponible: ${saldo:.2f}')
        ext=float(input('Dinero a extraer: $'))
        if ext<=saldo:
            saldo=saldo-ext
            print(Style.BRIGHT+Back.WHITE+Fore.GREEN+'OPERACION EXITOSA!!!')
        else:
            print(Style.BRIGHT+Fore.RED+Back.WHITE+'LA EXTRACCION EXCEDE EL SALDO!'.center(50,' '))
            print(Style.BRIGHT+Fore.RED+Back.WHITE+'OPERACION IMPOSIBLE'.center(50,' '))

titulo()
cajero()
gracias()