'''''
Clasificación de ángulos
 Solicita al usuario el valor de un ángulo en grados y 
 determina si es agudo (<90°), recto (90°), obtuso (>90° y <180°) o llano (180°).
'''''

# Dato

angulo = int(input('Ingresar un angulo: '))

# Cuerpo

if angulo < 0:
    print ('Angulo no valido')
elif angulo < 90:
    print (f'El angulo {angulo} es agudo.')
elif angulo == 90:
    print (f'El angulo {angulo} es Recto.')
elif angulo > 90 and angulo < 180:
    print (f'El angulo {angulo} es obtuso.')
elif angulo == 180:
    print (f'el angulo {angulo} es llano.')
else:
    print ('Angulo no valido')