'''''
Diseña un programa que permita registrar nombres y teléfonos. Al buscar un nombre, debe mostrar todos los números asociados.
'''''

# Agenda de contactos: nombre -> lista de teléfonos
agenda = {}

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    if nombre in agenda:
        agenda[nombre].append(telefono)
    else:
        agenda[nombre] = [telefono]

# Función para buscar un contacto
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Teléfonos de {nombre}:")
        for numero in agenda[nombre]:
            print(f"- {numero}")
    else:
        print(f"No se encontró a {nombre} en la agenda.")

# Menú interactivo
while True:
    print("\n--- Agenda Telefónica ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        agregar_contacto(nombre, telefono)
        print("Contacto guardado con éxito.")
    
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        buscar_contacto(nombre)
    
    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
