'''''
Crea un programa que registre las ventas diarias como tuplas (día, monto) dentro de una lista. Al final, muestra el total y el día con mayor venta.
'''''

# Lista para guardar las ventas como tuplas (día, monto)
ventas = []

print("=== Registro de Ventas Diarias ===")
print("Escribe 'fin' para terminar.\n")

# Registro interactivo de ventas
while True:
    dia = input("Día: ")
    if dia.lower() == "fin":
        break
    try:
        monto = float(input("Monto de la venta: "))
        ventas.append((dia, monto))
    except ValueError:
        print("Por favor, ingresa un número válido para el monto.")

# Calcular total y día con mayor venta
if ventas:
    total = sum(monto for _, monto in ventas)
    dia_mayor, mayor_venta = max(ventas, key=lambda x: x[1])

    print("\n--- Resumen de Ventas ---")
    print(f"Ventas registradas: {ventas}")
    print(f"Total vendido: ${total:.2f}")
    print(f"Día con mayor venta: {dia_mayor} (${mayor_venta:.2f})")
else:
    print("\nNo se registraron ventas.")
