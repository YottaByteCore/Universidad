# Solicitar la nota al usuario
nota = input("Escribe una nota para agregar al archivo: ")

# Abrir el archivo en modo append (agregar al final), crea el archivo si no existe
with open('notas.txt', 'a', encoding='utf-8') as archivo:
    archivo.write(nota + '\n')  # Agregar la nota con salto de línea

print("Nota agregada correctamente en 'notas.txt'.")
