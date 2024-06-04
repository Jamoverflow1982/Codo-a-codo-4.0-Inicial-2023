"""Desafío 1: Diccionario de datos personales
Desarrollar un diccionario que contenga datos no reales de una persona. El
diccionario debe tener los tipos de datos vistos (enteros, flotantes, cadenas,
lógicos, listas). Luego mostrar esos datos en formato de tarjeta, utilizando
métodos de cadenas y f-strings para concatenar datos, convertir a mayúsculas y
minúsculas, etc."""

from colorama import Back,Fore,Style,init
init(autoreset=True)

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

for titulo, dato in tarjeta_personal.items():
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
