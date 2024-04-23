print('='*80)
print(' FACTURADOR '.center(80,'='))
print(' by J. Monzon'.rjust(80,'='))
print()

print('DATOS DE FACTURACION')
razon=input('Ingrese razon social: ')
domi=input('Ingrese domicilio: ')
print()
print('PRODUCTO A FACTURAR')
desc=input('Descripcion de producto: ')
cant=int(input('Cantidad: '))
precio=float(input('Precio: $'))
off=float(input('Ingrese descuento: $'))
print()

total=cant*precio
totalci=total*1.21
totalcd=totalci-off
total3c=((totalcd*15)/100)+totalcd
total6c=((totalcd*25)/100)+totalcd

print('_'*80)
print()
print('DATOS DEL CLIENTE')
print('Razon social:', razon)
print('Domicilio:', domi)
print()
print('DETALLES DE LA COMPRA')
print('Cantidad\t\tDescripcion\t\tP.U.\t\tSubtotal')
print(f'{cant}\t\t\t{desc}\t\t${precio:.2f}\t\t${total:.2f}')
print()
print('CALCULOS ADICIONALES')
print(f'IVA (21%)           \t${totalci:.2f}')
print(f'Descuento Aplicado: \t${off:.2f}')
print(f'Total a pagar:      \t${totalcd:.2f}')
print()
print('FORMA DE PAGO')
print(f'1.CONTADO              \t${totalcd:.2f}')
print(f'2.CUOTAS (15% Interes) \t${total3c:.2f}')
print(f'3.CUOTAS (25% Interes) \t${total6c:.2f}')
print()
print('¡Gracias por su compra!')
print()