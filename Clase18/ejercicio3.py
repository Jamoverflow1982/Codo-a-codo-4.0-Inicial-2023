"""
Desarrollar dos funciones: la primera imprimirá los datos de la película (nombre,
día y hora, sala), solicitados por teclado. La segunda función obtendrá el valor
del ticket, recibiendo como parámetros la cantidad de entradas, el valor de la
entrada y un descuento en 10% sobre el total si la cantidad de entradas es mayor
o igual a 5
"""

off=10 #Descuento

def titulo():
    print('*'*50)
    print(' CINES CAC '.center(50,'*'))
    print(' by J. Monzon '.rjust(50,'*'))
    print()

def datos_pelicula(nombre, dia, hora, sala):
    print('*'*50)
    print(f'Nombre de la pelicula: {nombre}'.center(50,' '))
    print(f'Dia: {dia} Hora: {hora}'.center(50,' '))
    print(f'Sala: {sala}'.center(50,' '))
    print('*'*50)

def entrada(precio, cant, off):
    total=precio*cant
    total_des=total-((total*off)/100)
    print(f'Cantidad de entradas: {cant}'.center(50,' '))
    if cant>=5:
        print('-'*50)
        print(f' USTED POSEE UN {off}% DE DESCUENTO '.center(50,'-'))
        print('-'*50)
        print(f'El total a abonar es: ${total_des:.2f}'.center(50,' '))
        print('*'*50)
    else:
        print(f'El total a abonar es: ${total:.2f}'.center(50,' '))
        print('*'*50)

nombre=input('Ingrese nombre de la pelicula: ')
dia=input('Ingrese el dia de la funcion: ')
hora=input('Horario: ')
sala=input('Sala: ')
precio=float(input('Ingrese el precio de la entrada: $'))
cant=int(input('Cantidad de entradas: '))
print()
titulo()
datos_pelicula(nombre, dia, hora, sala)
entrada(precio, cant, off)