"""
Escribe un programa en Python que solicite al usuario el monto total de la
compra y la cantidad de artículos que está comprando. El programa debe
determinar el descuento aplicable según las siguientes reglas:
Si la cantidad de artículos comprados es mayor o igual a 5 y el monto
total es mayor a $10000, aplica un descuento del 15%.
Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a
3, aplica un descuento del 10%.
Si la cantidad de artículos comprados es menor a 3, no se aplica
descuento.
Al final, el programa debe imprimir el monto total de la compra después de
aplicar cualquier descuento o simplemente el monto original si no hay
descuento.
"""

off1=15 #Descuento mas 5 articulos
off2=10 #Descuento 3 a 5 articulos

def titulo():
    print('='*50)
    print(' DESCUENTO POR PRECIO Y CANTIDAD '.center(50,'='))
    print(' by J. Monzon '.rjust(50,'='))
    print()

def compra(cant, monto):
    if cant>=5 and monto>=10000:
        total=monto-((monto*off1)/100)
        print(f' USTED POSEE UN DESCUENTO DEL {off1}% '.center(50,'*'))
        print(f'El total de la compra es ${total:.2f}')
        print()
        print('GRACIAS POR SU COMPRA!!!'.center(50,' '))
    elif cant>=3 and cant<5:
        total=monto-((monto*off2)/100)
        print(f' USTED POSEE UN DESCUENTO DEL {off2}% '.center(50,'*'))
        print(f'El total de su compra es ${total:.2f}')
        print()
        print('GRACIAS POR SU COMPRA!!!'.center(50,' '))
    else:
        print(f'El total de su compra es ${monto:.2f}')
        print()
        print('GRACIAS POR SU COMPRA!!!'.center(50,' '))

titulo()
cant=int(input('Ingrese la cantidad de articulos comprados: '))
monto=float(input('Ingrese el valor total de la compra: $'))
print()
compra(cant, monto)
print()