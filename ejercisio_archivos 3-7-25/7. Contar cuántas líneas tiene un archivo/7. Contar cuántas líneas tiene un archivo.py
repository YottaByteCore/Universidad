# Abrimos el archivo en modo lectura
with open('poema.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()  # Leemos todas las líneas en una lista

# Contamos cuántas líneas hay
cantidad_lineas = len(lineas)

print("El archivo contiene", cantidad_lineas, "líneas.")
