def contar_palabras_en_archivo(nombre_archivo):
    total_palabras = 0
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = linea.split()  # Divide la línea en palabras usando espacios
                total_palabras += len(palabras)
        return total_palabras
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

archivo = 'frases.txt'
resultado = contar_palabras_en_archivo(archivo)

if resultado is not None:
    print(f"El archivo '{archivo}' tiene un total de {resultado} palabras.")
