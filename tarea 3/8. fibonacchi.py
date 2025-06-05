'''''
Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término, 
donde el valor de n lo ingresa el usuario, utilizando un bucle for.
'''''

# Pedimos al usuario el número de términos
n = int(input("Ingresa el número de términos de la serie de Fibonacci: "))

# Validamos que el número sea positivo
if n <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Inicializamos los dos primeros términos de la serie
    a, b = 0, 1
    print("Serie de Fibonacci hasta el término", n, ":")

    for i in range(n):
        print(a)
        a, b = b, a + b  # Actualizamos los valores para el siguiente término
