# Inicializamos la variable suma
suma_total = 0

# Abrimos el archivo en modo lectura
with open('datos.txt', 'r') as archivo:
    for linea in archivo:
        numero = int(linea.strip())  # Quitamos espacios y convertimos a entero
        suma_total += numero

print("La suma total es:", suma_total)
