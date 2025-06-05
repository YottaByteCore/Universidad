'''''
5. Escribe un programa que pida al usuario un número entero y luego imprima todos los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.
'''''

# Pedir al usuario un número entero
numero = int(input("Escribe un número entero: "))

# Imprimir los números en orden descendente hasta 0
while numero >= 0:
    print(numero)
    numero -= 1  # Restar 1 en cada paso
