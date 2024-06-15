"""
Desafío 1: Administración de empleados
Una empresa desea organizar en un diccionario los datos básicos de sus
empleados. Los datos que releva son: a) Nro legajo; b) Apellido y nombre; c) DNI;
d) Domicilio. La empresa tiene por el momento 5 empleados. Se pide:
a) Generar una lista de 5 elementos, cada uno con un diccionario con datos
ficticios.
b) Programar funciones que permitan:
i) Obtener un listado en formato de “tabla” de los empleados.
ii) Dar de alta un empleado
iii) Dar de baja un empleado
iv) Actualizar el domicilio
v) Acceder a alguna de las 4 operaciones anteriores
"""
from colorama import Style, Back, Fore, init
init (autoreset=True)
import os

screen='clear' #si es en windows cambiar por cls

def mostrarLista(legajos):
    print(Back.BLUE+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.BLUE+Style.BRIGHT+Fore.WHITE+'LISTA DE EMPLEADOS'.center(93,' '))
    print(Back.BLUE+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.LIGHTBLACK_EX+Fore.WHITE+' ___________________________________________________________________________________________ ')
    print(Back.LIGHTBLACK_EX+Fore.WHITE+Style.BRIGHT+'| Legajo |    Apellido    |     Nombre     |    DNI     |             Domicilio             |')
    print(Back.LIGHTBLACK_EX+Fore.WHITE+'|--------+----------------+----------------+------------+-----------------------------------|')
    for empleado in legajos:
        print(Back.LIGHTBLACK_EX+Fore.WHITE+f'|{empleado["leg"]:8}|{empleado["apellido"]:16}|{empleado["nombre"]:16}|{empleado["dni"]:12}|{empleado["domicilio"]:35}|')
    print(Back.LIGHTBLACK_EX+Fore.WHITE+' --------+----------------+----------------+------------+----------------------------------- ')
    print()

def altaEmpleado(legajo):
    i=0
    print(Back.LIGHTGREEN_EX+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.LIGHTGREEN_EX+Style.BRIGHT+Fore.WHITE+'ALTA DE EMPLEADO'.center(93,' '))
    print(Back.LIGHTGREEN_EX+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print()
    while True:
        legnuevo=(legajo[(len(legajo)-1)]['leg'])+1
        nombre=input('Ingrese nombre: ').capitalize()
        apellido=input('Ingrese apellido: ').capitalize()
        dni=int(input('Ingrese DNI (solo numeros): '))
        domicilio=input('Ingrese el domicilio: ')
        nuevo={'leg': legnuevo, 'apellido': apellido, 'nombre': nombre, 'dni': dni, 'domicilio': domicilio}
        legajo.append(nuevo)
        print()
        i+=1
        op=input('Desea agregar otro legajo? (S/N): ').upper()
        if op == 'N':
            print()
            print(f'Se cargaron con exito {i} legajo(s)')
            print()
            break
        print()

def bajaEmpleado():
    print(Back.RED+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.RED+Style.BRIGHT+Fore.WHITE+'BAJA DE EMPLEADO'.center(93,' '))
    print(Back.RED+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    while True:
        indiceleg()
        print()
        opBaja=int(input('Ingrese una opcion para la baja: '))
        match opBaja:
            case 1:
                clave='leg'
                valor=int(input('Ingrese el numero: '))
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    baja(resbus, datosEmpleados)
            case 2:
                clave='nombre'
                valor=input('Ingrese el nombre: ').capitalize()
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    baja(resbus, datosEmpleados)
            case 3:
                clave='apellido'
                valor=input('Ingrese el apellido: ').capitalize()
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    baja(resbus, datosEmpleados)
            case 4:
                clave='dni'
                valor=int(input('Ingrese el DNI: '))
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    baja(resbus, datosEmpleados)
            case _:
                print('EL VALOR INGRESADO NO ES VALIDO!(')
        print()
        salir=input('Desea realizar otra baja? (S/N): ').upper()
        if salir=='N':
            print()
            break

def busqueda(legajo, clave, valor):
    i=0
    lista=[]
    while i < len(legajo): #Busca en todos los valores del diccioario y agrega los resultados a lista
        if valor==legajo[i][clave]:
            lista.append(i)
        i+=1
    print()
    if len(lista) == 0:
        print('No se encontro resultado!')
        print()
        valorLeg=0
    elif len(lista) == 1:
        print('Se encontro un resultado!')
        print()
    else:
        print(f'Se encontraron {len(lista)} resultados!')
        print()
    
    if len(lista)==1: #Si el valor encontrado es uno lo muestra, sino sigue
        print(f'Legajo: {legajo[lista[0]]["leg"]} - Nombre: {legajo[lista[0]]["nombre"]} {legajo[lista[0]]["apellido"]} - DNI: {legajo[lista[0]]["dni"]} - Domicilio: {legajo[lista[0]]["domicilio"]}')
        print()
        valorLeg=lista[0]
    elif len(lista)>1:#Muestra los valores del la lista
        pase=0
        i=0
        for emp in lista:
            i+=1
            print(f'{i} - Legajo: {legajo[emp]["leg"]} - Nombre: {legajo[emp]["nombre"]} {legajo[emp]["apellido"]} - DNI: {legajo[emp]["dni"]} - Domicilio: {legajo[emp]["domicilio"]}')
        print()
        while pase != 1:
            op=int(input('Elija un empleado para operar: '))
            if op<=i and op>=1:
                valorLeg=lista[op-1]
                pase=1
            else:
                print()
                print('No ingreso una opcion valida!')
                print('Vuelva a intentarlo')
                print()
    return valorLeg

def baja(emp, legajo):
    op=input('Desea eliminar el legajo (S/N): ').upper()
    if op=='S':
        legajo.remove(legajo[emp])
        print()
        print('Legajo eliminado con exito!')
        print()
    else:
        print()
        print('NO se elimino el legajo!')
        print()

def actDatos(legajo):
    print(Back.YELLOW+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.YELLOW+Style.BRIGHT+Fore.WHITE+'LISTA DE EMPLEADOS'.center(93,' '))
    print(Back.YELLOW+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    while True:
        print('Busqueda de empleado')
        print()
        indiceleg()
        print()
        opBuscar=int(input('Ingrese una opcion para la busqueda: '))
        match opBuscar:
            case 1:
                clave='leg'
                valor=int(input('Ingrese el numero: '))
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    actualiza(resbus, datosEmpleados)
            case 2:
                clave='nombre'
                valor=input('Ingrese el nombre: ').capitalize()
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    actualiza(resbus, datosEmpleados)
            case 3:
                clave='apellido'
                valor=input('Ingrese el apellido: ').capitalize()
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    actualiza(resbus, datosEmpleados)
            case 4:
                clave='dni'
                valor=int(input('Ingrese el DNI: '))
                resbus=busqueda(datosEmpleados, clave, valor)
                if resbus>0:
                    actualiza(resbus, datosEmpleados)
            case _:
                print('EL VALOR INGRESADO NO ES VALIDO!')
        print()
        salir=input('Desea modificar otro legajo? (S/N): ').upper()
        if salir=='N':
            print()
            break

def indiceleg():
    print()
    print('1 - Legajo')
    print('2 - Nombre')
    print('3 - Apellido')
    print('4 - Documento de identidad')

def actualiza(emp, legajo):
    print('Que dato desea modificar?')
    indiceleg()
    print('5 - Domicilio')
    print()
    while True:
        op=int(input('Elija una opcion: '))
        match op:
            case 1:
                nuevoValor=int(input('Ingrese el nuevo numero de legajo: '))
                viejoValor=legajo[emp]["leg"]
                legajo[emp]["leg"]=nuevoValor
                print()
                print('Modificacion realizada con exito!')
                print(f'El valor {viejoValor} se reemplazo por {nuevoValor}')
                break
            case 2:
                nuevoValor=input('Ingrese el nuevo nombre: ').capitalize()
                viejoValor=legajo[emp]["nombre"]
                legajo[emp]["nombre"]=nuevoValor
                print()
                print('Modificacion realizada con exito!')
                print(f'El valor {viejoValor} se reemplazo por {nuevoValor}')
                break
            case 3:
                nuevoValor=input('Ingrese el nuevo apellido: ').capitalize()
                viejoValor=legajo[emp]["apellido"]
                legajo[emp]["apellido"]=nuevoValor
                print()
                print('Modificacion realizada con exito!')
                print(f'El valor {viejoValor} se reemplazo por {nuevoValor}')
                break
            case 4:
                nuevoValor=int(input('Ingrese el nuevo documento: '))
                viejoValor=legajo[emp]["dni"]
                legajo[emp]["dni"]=nuevoValor
                print()
                print('Modificacion realizada con exito!')
                print(f'El valor {viejoValor} se reemplazo por {nuevoValor}')
                break
            case 5:
                nuevoValor=input('Ingrese el nuevo domicilio: ').capitalize()
                viejoValor=legajo[emp]["domicilio"]
                legajo[emp]["domicilio"]=nuevoValor
                print()
                print('Modificacion realizada con exito!')
                print(f'El valor {viejoValor} se reemplazo por {nuevoValor}')
                break
            case _:
                print('EL VALOR INGRESADO NO ES VALIDO!')

datosEmpleados = [
    {'leg': 1, 'apellido': 'Perez', 'nombre': 'Juan', 'dni': 12223334, 'domicilio': 'Av de Los palotes 112 - Cap Fed'},
    {'leg': 2, 'apellido': 'Garcia', 'nombre': 'Laura', 'dni': 15434588, 'domicilio': 'A veces en la casa'},
    {'leg': 3, 'apellido': 'Fernandez', 'nombre': 'Pedro', 'dni': 20123433, 'domicilio': 'Donde dobla el viento'},
    {'leg': 4, 'apellido': 'Moreno', 'nombre': 'Luis', 'dni': 17343690, 'domicilio': 'Hijo del viento 1990 - Italia'},
    {'leg': 5, 'apellido': 'Gonzalez', 'nombre': 'Jose', 'dni': 11098456, 'domicilio': 'D10S hay uno solo - MARADO'},
    {'leg': 6, 'apellido': 'Garcia', 'nombre': 'Diego', 'dni': 22098456, 'domicilio': 'Solo Dios sabe'}
]
os.system(screen)
while True:
    print(Back.CYAN+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print(Back.CYAN+Style.BRIGHT+Fore.WHITE+'ADMINISTRACION DE EMPLEADOS'.center(93,' '))
    print(Back.CYAN+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
    print()
    print('1 - Mostrar lista de empleados')
    print('2 - Dar de alta un empleado')
    print('3 - Dar de baja un empleado')
    print('4 - Actualizar datos de un empleado')
    print('5 - Salir')
    print()
    op=int(input('Elije una opcion: '))
    match op:
        case 1:
            os.system(screen)
            mostrarLista(datosEmpleados)
        case 2:
            os.system(screen)
            altaEmpleado(datosEmpleados)
        case 3:
            os.system(screen)
            bajaEmpleado()
        case 4:
            os.system(screen)
            actDatos(datosEmpleados)
        case 5:
            os.system(screen)
            print()
            print(Back.LIGHTMAGENTA_EX+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
            print(Back.LIGHTMAGENTA_EX+Style.BRIGHT+Fore.WHITE+'GRACIAS POR UTILIZAR MI PROGRAMA'.center(93,' '))
            print(Back.LIGHTMAGENTA_EX+Style.BRIGHT+Fore.WHITE+''.center(93,' '))
            break
        case _:
            print()
            print('OPCION INVALIDA')
            print('INGRESE UN VALOR DE LA LISTA O 5 PARA SALIR')
            print()