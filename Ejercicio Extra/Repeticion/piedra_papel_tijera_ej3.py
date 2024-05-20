"""
3- Mejorar el juego Piedra, Papel o Tijera.
Usar un acumulador para sumar las veces que gana cada uno.
Repetir el juego hasta que el usuario desee salir.
Cuando termine la repetición, mostrar resultados de partidas ganadas por cada uno.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)
import random

def gracias():
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print(' GRACIAS POR UTILIZAR MI PROGRAMA '.center(80,'#'))
    print(Fore.LIGHTBLUE_EX+' by J. Monzon '.rjust(80,'#'))
    print()

def titulo():
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print(' PIEDRA PAPEL O TIJERA '.center(80,'#'))
    print(Fore.LIGHTBLUE_EX+'#'*80)
    print()

def juego():
    cpu=0
    usuario=0
    empate=0
    salir=1
    while salir!=0:
        print('Opcion 1 = PIEDRA\nOpcion 2 = PAPEL\nOpcion 3 = TIJERA\nOpcion 0 = Para Salir')
        eleccion=int(input('Ingrese su eleccion: '))
        compu=random.randint(1,3)
        match eleccion:
            case 0:
                salir=0
            case 1:
                if eleccion==compu:
                    empate+=1
                    print('Yo eleji PIEDRA!'.center(80,' '))
                    print('EMPATAMOS!!!\n'.center(80,' '))
                elif compu==2:
                    print('Yo eleji PAPEL!'.center(80,' '))
                    cpu+=1
                    print('GANE!!!'.center(80,' '))
                else:
                    usuario+=1
                    print('Yo eleji TIJERA!'.center(80,' '))
                    print('PERDI! =('.center(80,' '))
            case 2:
                if eleccion==compu:
                    empate+=1
                    print('Yo eleji PAPEL!'.center(80,' '))
                    print('EMPATAMOS!!!\n'.center(80,' '))
                elif compu==3:
                    cpu+=1
                    print('Yo eleji TIJERA!'.center(80,' '))
                    print('GANE!!!'.center(80,' '))
                else:
                    print('Yo eleji PIEDRA!'.center(80,' '))
                    usuario+=1
                    print('PERDI! =('.center(80,' '))
            case 3:
                if eleccion==compu:
                    empate+=1
                    print('Yo eleji TIJERA!'.center(80,' '))
                    print('EMPATAMOS!!!\n'.center(80,' '))
                elif compu==1:
                    cpu+=1
                    print('Yo eleji PIEDRA!'.center(80,' '))
                    print('GANE!!!'.center(80,' '))
                else:
                    usuario+=1
                    print('Yo eleji PAPEL!'.center(80,' '))
                    print('PERDI! =('.center(80,' '))
            case _:
                print(Fore.LIGHTRED_EX+'EL NUMERO INGRESADO NO ES EL CORRECTO!!!'.center(80,'*'))
                print(Fore.LIGHTRED_EX+'INGRESE UN NUMERO ENTRE 1 Y 3 O 0 (CERO) PARA SALIR'.center(80,'*'))
    return usuario, cpu, empate

titulo()
usu, cpu, emp=juego()
print()
print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'*'*80)
print(Style.BRIGHT+f'RESULTADO FINAL:'.center(80,' '))
print(Style.BRIGHT+f'Tus partidos ganados: {usu}'.center(80,' '))
print(Style.BRIGHT+f'Los que yo gane: {cpu}'.center(80,' '))
print(Style.BRIGHT+f'Empatados: {emp}'.center(80,' '))
print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'*'*80)
gracias()
