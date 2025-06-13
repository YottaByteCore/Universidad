'''''
Elabora un programa que permita registrar la asistencia de estudiantes por día en una clase. 
Luego, muestra cuántas veces asistió cada estudiante.
'''''

# Diccionario para registrar asistencia: nombre -> número de asistencias
asistencia = {}

# Lista de estudiantes (puedes modificarla o dejar que el usuario la ingrese)
estudiantes = ["Ana", "Luis", "Carlos", "Sofía", "Pedro"]

# Ciclo para registrar asistencia por día
while True:
    print("\n--- Registro de asistencia ---")
    print("Escribe 'fin' para terminar el registro del día.")
    
    for estudiante in estudiantes:
        while True:
            respuesta = input(f"¿{estudiante} asistió hoy? (s/n): ").lower()
            if respuesta == 's':
                asistencia[estudiante] = asistencia.get(estudiante, 0) + 1
                break
            elif respuesta == 'n':
                asistencia.setdefault(estudiante, 0)
                break
            else:
                print("Por favor, responde con 's' (sí) o 'n' (no).")
    
    continuar = input("\n¿Registrar otro día? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar resumen de asistencias
print("\n--- Resumen de asistencia ---")
for estudiante, veces in asistencia.items():
    print(f"{estudiante}: {veces} asistencias")
