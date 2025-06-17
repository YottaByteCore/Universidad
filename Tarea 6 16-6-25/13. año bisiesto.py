'''''
Verificación de año bisiesto
 Solicita al usuario un año y determina si es bisiesto o no. 
 (Es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por 400).
'''

# Datos

año = int(input('Ingresar un año: '))

# Cuerpo
# Voy a poner que los años validos comienzen desde los años 2000 hacia adelante

if año > 2000:
    if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        print ('Es un año bisiesto')
    else:
        print ('El año no es bisiesto')
else:
    print ('El año no es valido, segun lo determino el Operador Oscar peña')