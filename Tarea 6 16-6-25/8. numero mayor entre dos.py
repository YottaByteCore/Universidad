'''''
Número mayor entre dos
 Pide al usuario que ingrese dos números y determina cuál es el mayor o si son iguales.
'''''

# Datos

numero = int(input('Ingresar el primer numero: '))
numero2 = int(input('Ingresar el segundo numero: '))

# Cuerpo

if numero == numero2:
    print ('Los numeros son iguales')
elif numero > numero2:
    print (f'El numero {numero} es mayor al numero {numero2} ')
else:
    print (f'El numero {numero2} es mayor al numero {numero}')