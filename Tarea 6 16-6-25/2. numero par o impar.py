'''''
Número par o impar
 Pide al usuario que ingrese un número entero y determina si es par o impar.
'''''

# Pedir numero

numero = int(input('Ingresar un numero'))


# Cuerpo

if numero %2:
    print ('No es par')
else:
    print('Es un numero par')