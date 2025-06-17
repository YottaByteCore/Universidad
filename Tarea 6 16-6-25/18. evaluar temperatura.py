'''''
Evaluación de temperatura
 Solicita la temperatura en grados Celsius e imprime un mensaje dependiendo del valor:
Menos de 0°C: “Hace mucho frío”
Entre 0°C y 20°C: “Clima fresco”
Entre 21°C y 30°C: “Clima agradable”
Más de 30°C: “Hace mucho calor”
'''''

# Solicitar la temperatura en grados Celsius
temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

# Evaluar el rango de la temperatura
if temperatura < 0:
    print("Hace mucho frío.")
elif 0 <= temperatura <= 20:
    print("Clima fresco.")
elif 21 <= temperatura <= 30:
    print("Clima agradable.")
else:
    print("Hace mucho calor.")
