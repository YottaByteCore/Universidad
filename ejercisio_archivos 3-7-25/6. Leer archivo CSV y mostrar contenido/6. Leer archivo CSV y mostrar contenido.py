# Abrimos el archivo en modo lectura
with open('estudiantes.csv', 'r', encoding='utf-8') as archivo:
    # Leemos todas las líneas
    lineas = archivo.readlines()

    # Saltamos la primera línea (encabezado)
    for linea in lineas[1:]:
        nombre, edad, calificacion = linea.strip().split(',')
        print(f"{nombre} tiene {edad} años y obtuvo una calificación de {calificacion}.")
