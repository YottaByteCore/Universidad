'''''
Crea un programa que registre temperaturas diarias durante una semana y calcule la media, la temperatura más alta y la más baja.
'''''

# Lista para almacenar las temperaturas
temperaturas = []

# Registrar temperaturas por día
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Registro de temperaturas diarias\n")
for dia in dias_semana:
    while True:
        try:
            temp = float(input(f"Temperatura del {dia}: "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Calcular estadísticas
media = sum(temperaturas) / len(temperaturas)
max_temp = max(temperaturas)
min_temp = min(temperaturas)

# Mostrar resultados
print("\n--- Resumen de la semana ---")
print(f"Temperaturas registradas: {temperaturas}")
print(f"Temperatura media: {media:.2f}°C")
print(f"Temperatura más alta: {max_temp:.2f}°C")
print(f"Temperatura más baja: {min_temp:.2f}°C")
