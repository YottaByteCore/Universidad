'''''
Define una clase Pelicula con atributos como título, director y género. Guarda varias películas en un diccionario con clave única.
'''''

# Definición de la clase Pelicula
class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.genero = genero

    def __str__(self):
        return f"'{self.titulo}' | Director: {self.director} | Género: {self.genero}"

# Diccionario para almacenar las películas
# Clave única (por ejemplo: ID o código): valor = objeto Pelicula
peliculas = {}

# Función para agregar una película
def agregar_pelicula():
    clave = input("ID único de la película: ")
    if clave in peliculas:
        print("Ya existe una película con ese ID.")
        return
    titulo = input("Título: ")
    director = input("Director: ")
    genero = input("Género: ")
    peliculas[clave] = Pelicula(titulo, director, genero)
    print("Película agregada correctamente.")

# Función para mostrar todas las películas
def mostrar_peliculas():
    if not peliculas:
        print("No hay películas registradas.")
        return
    print("\n--- Lista de películas ---")
    for clave, pelicula in peliculas.items():
        print(f"ID: {clave} → {pelicula}")

# Menú interactivo
while True:
    print("\n--- Catálogo de Películas ---")
    print("1. Agregar película")
    print("2. Mostrar todas las películas")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        agregar_pelicula()
    elif opcion == "2":
        mostrar_peliculas()
    elif opcion == "3":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
