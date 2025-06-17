'''''
Mayor entre tres números
 Pide al usuario tres números y muestra el mayor de ellos.
'''''

# Datos

numero = int(input('Ingresar el primer numero: '))
numero2 = int(input('Ingresar el segundo numero: '))
numero3 = int(input('Ingresar el tercero numero: '))


# Cuerpo

if numero == numero2 == numero3:
    print ('Los numeros son iguales')
elif numero >= numero2 and numero >= numero3:
    print (f'El numero {numero} es el mayor.')
elif numero2 >= numero and numero2 >= numero3:
    print (f'El numero {numero2} es el mayor')
else:
    print (f'El numero {numero3} es el mayor.')