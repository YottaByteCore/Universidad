'''''
Mayor de edad
 Solicita la edad de una persona e imprime si es mayor o menor de edad (mayor de 18 años).
'''''

# Dato

edad = int(input('Ingrese su edad: '))

# Cuerpo

if edad <= 0 or edad >= 100: # Añadi esto extra, como un tipo de limitador.
    print ('Edad no valido')
elif edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')