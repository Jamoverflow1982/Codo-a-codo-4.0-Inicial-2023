"""
Desafío 2: ABM de datos personales
Teniendo en cuenta el diccionario del desafío anterior, desarrollar un programa
que permita, a través de la carga de datos por teclado las siguientes acciones:
● Cargar un nuevo dato personal al diccionario.
● Modificar una clave y su correspondiente valor, ingresados por teclado.
● Eliminar una clave
Para realizar estas acciones realice un menú en el programa principal o utilice
funciones para gestionar estas operaciones. Recuerde colocar el diccionario
como parámetro en la declaración y como argumento en la llamada.
"""

from colorama import Back,Fore,Style,init
init(autoreset=True)
import os

def tarjeta(tar_per):
    for titulo, dato in tar_per.items():
        print(Style.BRIGHT+Back.BLUE+Fore.WHITE+f'{titulo.capitalize()} : '.rjust(15,' '), end='')
        if titulo == 'hijos': #espera al titulo hijos, ya que es una lista
            total=len(dato) #cuenta la cantidad de hijos
            for nombre in dato:
                total -=1 #resta un hijo por vuelta
                if total !=0: #controla hasta que llegue el ultimo asi hace el salto de linea
                    print(Style.BRIGHT+Back.RED+Fore.WHITE+f'{nombre.capitalize()}', end=Style.BRIGHT+Back.RED+Fore.WHITE+' ')
                else: 
                    print(Style.BRIGHT+Back.RED+Fore.WHITE+f'{nombre.capitalize()}'.ljust(12,' '))
        else:
            if type(dato) == str:
                print(Style.BRIGHT+Back.RED+Fore.WHITE+f'{dato.capitalize()}'.ljust(30,' '))
            else:
                print(Style.BRIGHT+Back.RED+Fore.WHITE+f'{dato}'.ljust(30,' '))

def carga(tar_per):
    while True:
        print()
        print(Back.CYAN+Fore.WHITE+'CARGA DE NUEVO VALOR'.center(50,' '))
        clave=input('Ingrese el nombre de la clave: ')
        valor=input('Ingrese el valor de la clave: ')
        op=input(Back.LIGHTRED_EX+'Esta seguro de guardar los nuevos datos (S - N): ')
        op=op.upper()
        if op == 'S':
            print()
            tar_per[clave]=valor
            tarjeta(tar_per)
            break
        else:
            break

def modif_cla(tar_per):
    valores=[]
    i=0
    print()
    print(Back.GREEN+Fore.WHITE+'MODIFICACION DE VALOR DE CLAVE'.center(50,' '))
    for claves in tar_per.keys():
        i +=1
        valores.append(claves)
        print(f'{i} - {claves}')
    while True:
        print()
        op=int(input('Ingrese un numero de opcion para modificar: '))
        if op >= 0 and op <= i:
            print(f'Usted va a modificar la clave: {valores[op-1]}')
            val=input('Ingrese un nuevo valor: ')
            op2=input(Back.LIGHTRED_EX+'Esta seguro de modificar los datos (S - N): ')
            op2=op2.upper()
            if op2 == 'S':
                print()
                tar_per[valores[op-1]]=val
                tarjeta(tar_per)
                break
            else:
                break
        else:
            print('EL NUMERO INGRESADO NO ES UNA OPCION VALIDA')
            print('VUELVA A INGRESAR LA OPCION')

def eliminar(tar_per):
    valores=[]
    i=0
    print()
    print(Back.RED+Fore.WHITE+'ELIMINACION DE CLAVES'.center(50,' '))
    for claves in tar_per.keys():
        i +=1
        valores.append(claves)
        print(f'{i} - {claves}')
    while True:
        op=int(input('Ingrese un numero de opcion para eliminar: '))
        if op >= 0 and op <= i:
            print(f'Usted va a eliminar la clave: {valores[op-1]}')
            op2=input(Back.LIGHTRED_EX+'Esta seguro de eliminar los datos (S - N): ')
            op2=op2.upper()
            if op2 == 'S':
                tar_per.pop(valores[op-1])
                tarjeta(tar_per)
                break
            else:
                break

tarjeta_personal={
    'nombre':'javier',
    'apellido':'monzon',
    'dni':29298661,
    'direccion':'constitucion',
    'numero':2678,
    'localidad':'victoria',
    'cp':1646,
    'hijos':['tiziano', 'valentino', 'agostina']
}

#MENU PRINCIPAL
os.system('clear') #clear para mac o linux o cls para windows
print(Style.BRIGHT+Back.CYAN+Fore.WHITE+'EDITOR DE TARJETA'.center(50,' '))

while True:
    print()
    print('1 - Cargar nuevo dato\n2 - Modificar clave\n3 - Eliminar clave\n4 - Vista de tarjeta\n5 - SALIR\n')
    op=int(input('Ingrese una opcion: '))
    match op:
        case 1:
            carga(tarjeta_personal)
        case 2:
            modif_cla(tarjeta_personal)
        case 3:
            eliminar(tarjeta_personal)
        case 4:
            tarjeta(tarjeta_personal)
        case 5:
            print(Back.GREEN+Fore.WHITE+Style.BRIGHT+'GRACIAS POR UTILIZAR MI PROGRAMA!!!'.center(50,' '))
            break
        case _:
            print(Back.RED+Fore.WHITE+Style.BRIGHT+f'{op} NO ES UNA OPCION VALIDA'.center(50,' '))
            print(Back.RED+Fore.WHITE+Style.BRIGHT+'VUELVA A INTENTARLO O INGRESE 6 PARA SALIR'.center(50,' '))