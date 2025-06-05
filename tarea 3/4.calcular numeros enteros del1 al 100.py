'''''
4. Escribe un programa que calcule la suma de todos los números enteros del 1 al 100 utilizando un bucle for.
'''''

# Inicializar la variable para guardar la suma
suma = 0

# Usar un bucle for para recorrer los números del 1 al 100
for numero in range(1, 101):
    suma += numero  # Sumar el número actual a la variable suma

# Mostrar el resultado
print("La suma de los números del 1 al 100 es:", suma)
