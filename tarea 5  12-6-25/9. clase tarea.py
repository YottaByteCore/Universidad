'''''
Crea una clase Tarea con nombre, prioridad y estado. Almacena las tareas en un diccionario y permite marcarlas como completadas.
'''''

# Clase Tarea
class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = "Pendiente"

    def marcar_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"{self.nombre} | Prioridad: {self.prioridad} | Estado: {self.estado}"

# Diccionario de tareas: id → Tarea
tareas = {}

# Función para agregar una tarea
def agregar_tarea():
    id_tarea = input("ID único para la tarea: ")
    if id_tarea in tareas:
        print("Ya existe una tarea con ese ID.")
        return
    nombre = input("Nombre de la tarea: ")
    prioridad = input("Prioridad (Alta, Media, Baja): ")
    tareas[id_tarea] = Tarea(nombre, prioridad)
    print("Tarea agregada correctamente.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\n--- Lista de Tareas ---")
    for id_tarea, tarea in tareas.items():
        print(f"ID: {id_tarea} → {tarea}")

# Función para marcar una tarea como completada
def completar_tarea():
    id_tarea = input("ID de la tarea a completar: ")
    if id_tarea in tareas:
        tareas[id_tarea].marcar_completada()
        print("Tarea marcada como completada.")
    else:
        print("No se encontró ninguna tarea con ese ID.")

# Menú principal
while True:
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        print("Saliendo del gestor. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
