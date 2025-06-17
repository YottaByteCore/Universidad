'''''
Número positivo, negativo o cero
 Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero
'''''
# solicitar numero

numero = int(input('Ingresar un numero: '))

# Cuerpo

if numero > 0:
    print(f'El numero {numero} es positivo')
elif numero < 0:
    print(f'El numero {numero} es negativo')
else:
    print(f'El numero {numero} es Cero')