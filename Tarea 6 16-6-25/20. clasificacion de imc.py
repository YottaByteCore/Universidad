'''''
Clasificación de IMC
 Solicita el peso (kg) y la altura (m) de una persona, calcula su Índice de Masa Corporal (IMC = peso / altura²) y clasifícalo:
<18.5: Bajo peso
18.5-24.9: Normal
25-29.9: Sobrepeso
30 o más: Obesidad
'''''

# Solicitar peso y altura
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el IMC con dos decimales
print(f"Tu IMC es: {imc:.2f}")

# Clasificar el IMC
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
