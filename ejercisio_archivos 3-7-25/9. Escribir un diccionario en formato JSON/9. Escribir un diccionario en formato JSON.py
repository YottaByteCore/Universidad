import json

# Creamos el diccionario
persona = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Santo Domingo'
}

# Escribimos el diccionario en un archivo JSON
with open('persona.json', 'w', encoding='utf-8') as archivo:
    json.dump(persona, archivo, indent=4, ensure_ascii=False)

print("Diccionario guardado en 'persona.json' correctamente.")
