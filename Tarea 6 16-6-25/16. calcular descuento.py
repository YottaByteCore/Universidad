'''''
Calculadora de descuentos
 Solicita el precio de un producto y aplica descuentos según el monto:
Menos de $50: sin descuento
Entre $50 y $100: 5%
Más de $100: 10%
'''''

# Solicitar el precio del producto
precio = float(input("Ingresa el precio del producto: "))

# Aplicar el descuento según el monto
if precio < 50:
    descuento = 0
elif 50 <= precio <= 100:
    descuento = 0.05
else:
    descuento = 0.10

# Calcular el monto con descuento
monto_descuento = precio * descuento
precio_final = precio - monto_descuento

# Mostrar resultados
print(f"Descuento aplicado: ${monto_descuento:.2f}")
print(f"Precio final: ${precio_final:.2f}")
