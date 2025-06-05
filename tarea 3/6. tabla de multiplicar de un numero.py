'''''
Escribe un programa que imprima la tabla de multiplicar de un número dado por el usuario, desde el 1 hasta el 10, utilizando un bucle for.
'''''

# Pedir al usuario un número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Usar un bucle for para multiplicar del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
