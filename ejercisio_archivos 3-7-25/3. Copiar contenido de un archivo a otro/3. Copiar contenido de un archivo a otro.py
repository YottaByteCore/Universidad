# Abrimos el archivo origen en modo lectura
with open('origen.txt', 'r', encoding='utf-8') as archivo_origen:
    contenido = archivo_origen.read()  # Leemos todo el contenido

# Abrimos (o creamos) el archivo copia en modo escritura
with open('copia.txt', 'w', encoding='utf-8') as archivo_copia:
    archivo_copia.write(contenido)  # Escribimos el contenido leído

print("El contenido fue copiado correctamente a 'copia.txt'")
