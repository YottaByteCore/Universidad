'''''
Implementa un sistema de inventario donde se pueda agregar, 
consultar y actualizar el stock de productos. Cada producto tendrá nombre, cantidad y precio.
'''''

# Inventario: clave = nombre del producto, valor = diccionario con cantidad y precio
inventario = {}

# Función para agregar un nuevo producto
def agregar_producto():
    nombre = input("Nombre del producto: ").capitalize()
    if nombre in inventario:
        print("Este producto ya existe. Usa la opción de actualizar.")
        return
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"{nombre} agregado al inventario.")
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar números para cantidad y precio.")

# Función para consultar un producto
def consultar_producto():
    nombre = input("Nombre del producto a consultar: ").capitalize()
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"{nombre} → Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
    else:
        print(f"{nombre} no está en el inventario.")

# Función para actualizar stock y precio
def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ").capitalize()
    if nombre in inventario:
        try:
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            inventario[nombre]['cantidad'] = nueva_cantidad
            inventario[nombre]['precio'] = nuevo_precio
            print(f"{nombre} actualizado correctamente.")
        except ValueError:
            print("Entrada inválida.")
    else:
        print(f"{nombre} no está en el inventario.")

# Función para mostrar todos los productos
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n--- Inventario Actual ---")
    for nombre, datos in inventario.items():
        print(f"{nombre}: Cantidad = {datos['cantidad']}, Precio = ${datos['precio']:.2f}")

# Menú principal
while True:
    print("\n--- Sistema de Inventario ---")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Mostrar todo el inventario")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        consultar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
