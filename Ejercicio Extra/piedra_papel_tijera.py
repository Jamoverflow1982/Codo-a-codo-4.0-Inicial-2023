cpu=2

def resolver(eleccion):
    if cpu==1:
        print(f'Yo eleji Piedra! {r1}!!!')
    elif cpu==2:
        print(f'Yo eleji Papel! {r2}!!!')
    else:
        print(f'Yo eleji Tijera {r3}!!!')

def juego (eleccion):
    if eleccion==1:
        usu='PIEDRA'
        p1='EMPATAMOS'
        p2='GANE'
        p3='PERDI'
    elif eleccion==2:
        usu='PAPEL'
        p2='EMPATAMOS'
        p3='GANE'
        p1='PERDI'
    else:
        usu='TIJERA'
        p3='EMPATAMOS'
        p1='GANE'
        p2='PERDI'
    return usu,p1,p2,p3

print('<'*50)
print('VAMOS A JUGAR!!!'.center(50,' '))
print('>'*50)
print()
print('1 - PIEDRA\n2 - PAPEL\n3 - TIJERA')
eleccion = int(input('Eleji una opcion: '))
print()

usuario, r1, r2, r3=juego(eleccion)
resolver(eleccion)
print()

