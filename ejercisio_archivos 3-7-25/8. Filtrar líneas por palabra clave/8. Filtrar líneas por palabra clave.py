# Abrimos el archivo en modo lectura
with open('log.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        if 'ERROR' in linea:
            print(linea.strip())  # Mostramos la línea sin saltos de línea extra
