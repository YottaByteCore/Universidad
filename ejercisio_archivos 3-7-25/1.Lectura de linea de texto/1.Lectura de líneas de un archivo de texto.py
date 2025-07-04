# Abrir el archivo en modo lectura
with open('nombres.txt', 'r', encoding='utf-8') as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        # Imprimir la línea eliminando el salto de línea final
        print(linea.strip())
