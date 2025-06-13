'''''
Crea un programa que almacene las calificaciones de varios estudiantes en distintas asignaturas usando diccionarios y listas.
 Permite calcular el promedio por estudiante y mostrar quién tiene la mejor nota
 '''''

# Programa para registrar calificaciones y calcular promedios

# Diccionario para guardar las notas de cada estudiante
calificaciones = {
    "Juan": {"Matemáticas": 85, "Historia": 90, "Ciencias": 78},
    "Sofía": {"Matemáticas": 92, "Historia": 88, "Ciencias": 95},
    "Carlos": {"Matemáticas": 75, "Historia": 70, "Ciencias": 72},
    "Lucía": {"Matemáticas": 88, "Historia": 91, "Ciencias": 89}
}

# Diccionario donde se guardará el promedio de cada estudiante
promedios = {}

# Recorremos cada estudiante para calcular su promedio
for nombre, materias in calificaciones.items():
    total_notas = sum(materias.values())
    cantidad_materias = len(materias)
    promedio = total_notas / cantidad_materias
    promedios[nombre] = promedio

# Mostramos el promedio de cada estudiante
print("Promedio de cada estudiante:\n")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")

# Buscamos quién tiene el mejor promedio
mejor_estudiante = max(promedios, key=promedios.get)
mejor_promedio = promedios[mejor_estudiante]

print(f"\nEl mejor promedio lo tiene {mejor_estudiante} con {mejor_promedio:.2f}")
