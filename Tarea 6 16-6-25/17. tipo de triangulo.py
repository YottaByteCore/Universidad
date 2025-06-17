'''''
Tipo de triángulo
 Pide tres longitudes y determina si el triángulo es equilátero, isósceles o escaleno.
'''''

# Solicitar las longitudes
lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer lado: "))

# Verificar si forman un triángulo (regla del triángulo)
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Determinar el tipo de triángulo
    if lado1 == lado2 == lado3:
        print("Es un triángulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("Las longitudes ingresadas NO forman un triángulo.")
