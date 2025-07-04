# Lista de números
numeros = [10, 20, 30, 40, 50]

# Abrimos (o creamos) el archivo en modo escritura
with open('numeros.txt', 'w') as archivo:
    for numero in numeros:
        archivo.write(str(numero) + '\n')  # Convertimos el número a texto y agregamos salto de línea

print("Los números se escribieron correctamente en 'numeros.txt'")
