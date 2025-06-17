'''''
Calificación aprobatoria
 Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o 
'''''

# Datos

calificacion = int(input('Ingresar su Calificacion: '))

# Cuerpo

if calificacion > 100 or calificacion < 0:
    print('Calificacion no valido')
elif calificacion >= 60:
    print(f'Tu calificacion {calificacion}, por lo tanto pasaste ')
else:
    print(f'Tu calificacion es menor al promedio {calificacion} por lo tanto no pasate')