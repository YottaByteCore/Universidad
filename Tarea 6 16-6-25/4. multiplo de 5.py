'''''
Múltiplo de 5
 Escribe un programa que pida un número y determine si es múltiplo de 5.
'''''

# Datos

numero = int(input('Ingresar un numero: '))

# Cuerpo

if numero %5 == 0:
    print(f'El numero {numero} es multiplo de 5.')
else:
    print(f'El numero {numero} no es multiplo de 5.')