"""
Escribe una función que tome tres números como argumentos y regrese el
mayor de ellos.
Tip: Utiliza comparaciones directas (condicionales) entre los números para
determinar cuál es el mayor.
"""

def titulo():
    print('+'*50)
    print(' NUMERO MAYOR '.center(50,'+'))
    print(' by J. Monzon '.rjust(50,'+'))
    print()
def mayor(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        num11=str(num1)
        mayor=" El mayor es "+num11+" "
    elif num2>=num1 and num2>=num3:
        num22=str(num2)
        mayor=" El mayor es "+num22+" "
    elif num3>=num1 and num3>=num2:
        num33=str(num3)
        mayor=" El mayor es "+num33+" "
    
    if num3==num2 and num2==num1:
        mayor=" Los tres numeros son iguales "
    return mayor

titulo()
print('Ingrese tres numeros...')
num1=int(input('Ingrese el primer numero:'))
num2=int(input('Ingrese el segundo numero: '))
num3=int(input('Ingrese el tercer numero: '))
print()
print('*'*50)
print(mayor(num1, num2, num3).center(50,'*'))
print('*'*50)
print()
