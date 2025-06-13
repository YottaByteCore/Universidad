'''''
Desarrolla una clase Libro con atributos como título, autor y año. 
Luego, crea una lista de libros y permite buscar por autor o año.
'''''

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.año})"

# Lista de libros
biblioteca = [
    Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
    Libro("1984", "George Orwell", 1949),
    Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985),
    Libro("Fahrenheit 451", "Ray Bradbury", 1953),
    Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981)
]

# Función para buscar libros por autor
def buscar_por_autor(autor):
    encontrados = [libro for libro in biblioteca if libro.autor.lower() == autor.lower()]
    if encontrados:
        print(f"\nLibros de {autor}:")
        for libro in encontrados:
            print(f"- {libro}")
    else:
        print(f"\nNo se encontraron libros del autor '{autor}'.")

# Función para buscar libros por año
def buscar_por_año(año):
    encontrados = [libro for libro in biblioteca if libro.año == año]
    if encontrados:
        print(f"\nLibros publicados en {año}:")
        for libro in encontrados:
            print(f"- {libro}")
    else:
        print(f"\nNo se encontraron libros del año {año}.")

# Menú interactivo
while True:
    print("\n--- Biblioteca Virtual ---")
    print("1. Buscar por autor")
    print("2. Buscar por año")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        autor = input("Nombre del autor: ")
        buscar_por_autor(autor)
    elif opcion == "2":
        try:
            año = int(input("Año de publicación: "))
            buscar_por_año(año)
        except ValueError:
            print("Por favor, ingresa un año válido.")
    elif opcion == "3":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
