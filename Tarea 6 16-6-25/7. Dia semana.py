'''''
Día de la semana
 Escribe un programa que solicite un número del 1 al 7 y muestre el día de la semana correspondiente (1 es lunes, 7 es domingo).
'''''

# Datos

dia = int(input('Ingrese un dia de la semana: '))

# Cuerpo

if dia == 1:
    print('Es lunes')
elif dia == 2:
    print('Es martes')
elif dia == 3:
    print ('Es miercoles')
elif dia == 4:
    print('Es jueves')
elif dia == 5:
    print ('Es Viernes')
elif dia == 6:
    print ('Es Sabado')
elif dia == 7:
    print ('Es Domingo')
else:
    print ('Dia de la semana no existente')