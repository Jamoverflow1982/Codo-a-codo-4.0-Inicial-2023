"""
3. Crear un programa que simule un “Cajero Automático”.
Al comenzar mostrar un mensaje de bienvenida.
Luego mostrar el mensaje “Ingrese su tarjeta y escriba el PIN para comenzar”. Si el PIN ingresado es correcto, mostrar el Menú de opciones, sino mostrar el mensaje “PIN incorrecto”. Puedes tener el PIN guardado en una variable.
El Menú de opciones:
1. Datos del Cliente
Esta opción mostrará por pantalla los datos del cliente que tendrás guardados en variables:
Nombre y apellido
CBU
Saldo
2. Saldo actual
Mostrará por pantalla el saldo disponible.
3. Realizar Depósito
Permitirá ingresar el monto, mostrar un mensaje de depósito realizado correctamente, e incrementar el saldo del cliente, que tendrás guardado en una variable, y que inicialmente será de 100000.
4. Realizar Extracción
Permitirá ingresar el monto, mostrar un mensaje de extracción realizada correctamente, y decrementar el saldo del cliente. Validar si el saldo disponible es suficiente para realizar la operación, caso contrario indicar saldo insuficiente.
5. Realizar Transferencia
Se podrá colocar CBU o Alias del destinatario y el monto a transferir, mostrar un mensaje de que la operación fue realizada con éxito y descontar el monto del saldo. 
6. Salir
Se mostrará la leyenda “No olvide extraer su tarjeta”. 
"""
from colorama import Back, Style, Fore, init
init(autoreset=True)

#Datos del cliente
pin=1234
nombre='Javier Monzon'
cbu=12345678910
saldo=100000

def bienvenida():
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'-'*80)
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+' C O D O  A  C O D O  4 . 0  B A N K '.center(80,'-'))
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+' C A J E R O  A U T O M A T I C O '.center(80,'-'))
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'-'*80)

def saludo():
    print()
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'-'*80)
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+' C O D O  A  C O D O  4 . 0  B A N K '.center(80,'-'))
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+' GRACIAS POR UTILIZAR NUESTROS SERVICIOS '.center(80,'-'))
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'-'*80)
    print()

def ingreso(pin):
    tarjeta=0
    cont=1
    pinval=0
    valtar=valpin=0
    print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'>'*80)
    print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'AL TERCER INTENTO DE INGRESO DE TARJETA SE ABORTA LA OPERACION'.center(80,' '))
    print(Style.BRIGHT+Back.WHITE+Fore.BLACK+f'Intentos de ingreso de tarjeta: {cont}'.center(80,' '))
    print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'<'*80)
    while tarjeta!=1:
        tar=input('\nIngreso su tarjeta [S/N]: ')
        print()
        tar=tar.upper()
        if tar=='S':
            tarjeta=cont=valtar=1
        else:
            cont+=1
        if cont>=4:
            print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
            print(Style.BRIGHT+Back.RED+Fore.WHITE+'* * * OPERACION CANCELADA * * *'.center(80,' '))
            print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
            print()
            valtar=0
            tarjeta=1
    if valtar==1:
        while pinval!=1:
            print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'>'*80)
            print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'AL TERCER INTENTO DE INGRESO DE PIN SE ABORTA LA OPERACION'.center(80,' '))
            print(Style.BRIGHT+Back.WHITE+Fore.BLACK+f'Intentos de ingreso de tarjeta: {cont}'.center(80,' '))
            print(Style.BRIGHT+Back.WHITE+Fore.BLACK+'<'*80)
            pinin=int(input('\nIngrese su PIN de cuatro digitos: '))
            print()
            if pinin==pin:
                print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
                print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'EL PIN INGRESADO ES CORRECTO!'.center(80,' '))
                print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
                pinval=valpin=1
            else:
                print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'EL PIN INGRESADO ES INCORRECTO!'.center(80,' '))
                print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
                cont+=1
            if cont>=4:
                print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'* * * OPERACION CANCELADA! * * *'.center(80,' '))
                print(Style.BRIGHT+Back.RED+Fore.WHITE+' '*80)
                print()
                valpin=0
                pinval=1
    return valpin

def opcion1():
    print()
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Titular de la cuenta: {nombre}'.ljust(80,' '))
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'CBU:                  {cbu}'.ljust(80,' '))
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Saldo:                ${saldo:.2f}'.ljust(80,' '))
    print()

def opcion2():
    print()
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Su saldo es de: ${saldo:.2f}'.ljust(80,' '))
    print()

def opcion3():
    global saldo
    dep=float(input('\nIngrese el monto a depositar: $'))
    saldo=saldo+dep
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'OPERACION REALIZADA CON EXITO!'.center(80,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
    print()
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Su saldo actualizado es de: ${saldo:.2f}'.center(80,' '))
    print()

def opcion4():
    global saldo
    dep=float(input('\nIngrese el monto a extraer: $'))
    saldo=saldo-dep
    print()
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'OPERACION REALIZADA CON EXITO!'.center(80,' '))
    print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
    print()
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Su saldo actualizado es de: ${saldo:.2f}'.center(80,' '))
    print()

def opcion5():
    global saldo
    salida=0
    print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'TRANSFERENCIA A TERCEROS'.center(80,' '))
    print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Su saldo es de: ${saldo:.2f}'.ljust(80,' '))
    while salida!=1:
        tracbu=int(input('Ingrese el CBU destino (tiene que tener 11 digitos): '))
        cbustr=str(tracbu)
        cbustr=len(cbustr)
        if cbustr==11:
            print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'CBU ACEPTADO!'.center(80,' '))
            salida=1
        else:
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+'La longitud del CBU no es la correcta!'.center(80,' '))
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+'Ingreselo nuevamente'.center(80,' '))
    while salida!=0:
        traval=float(input('\nIngrese el monto a transferir: $'))
        if traval<=saldo:
            print()
            print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
            print(Style.BRIGHT+Back.GREEN+Fore.WHITE+'OPERACION REALIZADA CON EXITO!'.center(80,' '))
            print(Style.BRIGHT+Back.GREEN+Fore.WHITE+' '*80)
            print()
            print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Se tranfirio al CBU      {tracbu}'.ljust(80,' '))
            print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'El monto de:            ${traval}'.ljust(80,' '))
            saldo=saldo-traval
            salida=0
            print()
            print(Style.BRIGHT+Back.WHITE+Fore.BLUE+f'Su saldo disponible es: ${saldo:.2f}'.ljust(80,' '))
        else:
            print()
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+'El monto excede el saldo'.center(80,' '))
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+'Ingrese otro monto'.center(80,' '))

def opciones():
    op=1
    while op!=6:
        print()
        print(Style.BRIGHT+Back.BLUE+Fore.WHITE+'INDIQUE LA OPERACION QUE QUIERE REALIZAR'.center(80,' '))
        print('\n1. Datos del Cliente\n2. Saldo actual\n3. Realizar Depósito\n4. Realizar Extracción\n5. Realizar Transferencia\n6. Salir\n')
        op=int(input('OPCION: '))
        match op:
            case 1:
                opcion1()
            case 2:
                opcion2()
            case 3:
                opcion3()
            case 4:
                opcion4()
            case 5:
                opcion5()
            case 6:
                saludo()
            case _:
                print(Style.BRIGHT+Back.RED+Fore.WHITE+f'{op} NO CORRESPONDE A UNA OPCION'.center(80,' '))
                print(Style.BRIGHT+Back.RED+Fore.WHITE+'Ingrese un numero de opcion valido'.center(80,' '))

bienvenida()
pinok=ingreso(pin)
if pinok==1:
    opciones()
else:
    saludo()


