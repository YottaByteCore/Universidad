'''''
Conversión de horas a turnos
 Pide la hora (0-23) y determina si es "Mañana" (6-11), "Tarde" (12-17), "Noche" (18-23) o "Madrugada" (0-5).
'''''

# Solicitar la hora (de 0 a 23)
hora = int(input("Ingresa la hora (0-23): "))

# Validar que la hora esté en el rango correcto
if 0 <= hora <= 23:
    if 6 <= hora <= 11:
        print("Mañana")
    elif 12 <= hora <= 17:
        print("Tarde")
    elif 18 <= hora <= 23:
        print("Noche")
    else:  # 0 a 5
        print("Madrugada")
else:
    print("Hora inválida. Debe ser entre 0 y 23.")
