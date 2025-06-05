'''''
3. Escribe un programa que pida al usuario un número entero positivo. El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.
'''''
# Pedir al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
while numero <= 0:
    numero = int(input("Por favor, introduce un número entero positivo: "))

# Inicializar el contador de dígitos
contador = 0

# Usar un bucle while para contar los dígitos
while numero > 0:
    numero = numero // 10  # Dividir entre 10 para eliminar el último dígito
    contador += 1          # Aumentar el contador en 1

# Mostrar el resultado
print("El número tiene", contador, "dígitos.")
