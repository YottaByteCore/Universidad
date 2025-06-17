'''''
Conversión de calificaciones
 Solicita la calificación numérica de un estudiante (0-100) y conviértela en una letra:
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''''

# Datos

Calificacion = int(input('Ingresa tu calificacion: '))

# Cuerpo

if Calificacion < 0 or Calificacion > 100:
    print ('¿En serio? Esa calificación ni existe, vuelve a intentarlo...')
elif Calificacion > 0 and Calificacion <= 59:
    print ('F: Eso fue un desastre total, nos vemos el año que viene')
elif Calificacion >= 60 and Calificacion <= 69:
    print ('D: Muy justo, y nada para celebrar. ¡A estudiar más duro!')
elif Calificacion >= 70 and Calificacion <= 79:
    print ('C: Pasaste, pero apenas. No te confíes.')
elif Calificacion >= 80 and Calificacion <= 89:
    print ('B: Bien, pero podrías hacerlo mucho mejor.')
else:
    print ('A: Felicidades, no todos llegan a este nivel, superaste a los otros perdedores')


