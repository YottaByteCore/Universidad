'''''
Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while. 
El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
'''''

# Pedimos al usuario un número entero no negativo
n = int(input("Ingresa un número entero no negativo: "))

# Validamos que el número no sea negativo
if n < 0:
    print("El número debe ser no negativo.")
else:
    factorial = 1
    contador = 1

    while contador <= n:
        factorial *= contador  # Multiplicamos el factorial por el contador
        contador += 1          # Avanzamos al siguiente número

    print(f"El factorial de {n} es {factorial}")
