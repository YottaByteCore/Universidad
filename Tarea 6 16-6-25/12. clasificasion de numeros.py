'''''
Clasificación de números
 Pide al usuario tres números y determina si son todos positivos, todos negativos, mixtos o si hay ceros.
'''''

# Datos

num1 = int(input('Ingresar el primer numero'))
num2 = int(input('Ingresar el segundo numero'))
num3 = int(input('Ingresar el tercero numero'))

# Cuerpo

if num1 == 0 or num2 == 0 or num3 == 0:
    print ('Hay numeros iguales a cero')
elif num1 > 0 and num2 > 0 and num3 > 0:
    print ('Los numeros son todos positivos')
elif num1 < 0 and num2 < 0 and num3 < 0:
    print ('Los numeros son negativos')
else:
    print ('Los numeros son mixtos')
