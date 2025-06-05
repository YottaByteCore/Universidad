'''''
7. Escribe un programa que pida al usuario un número entero positivo y luego imprima todos los números impares desde 1 hasta el número ingresado utilizando un bucle while.
'''''

# Pedimos al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Validamos que el número sea positivo
if numero <= 0:
    print("El número debe ser entero y positivo.")
else:
    # Inicializamos la variable con el primer número impar
    i = 1
    print("Números impares desde 1 hasta", numero, ":")
    while i <= numero:
        print(i)
        i += 2  # Avanzamos al siguiente número impar
