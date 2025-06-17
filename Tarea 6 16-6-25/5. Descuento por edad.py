'''''
Descuento por edad
 Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la edad del usuario y determina si aplica para el descuento.
'''''

# Dato

edad = int(input('Ingresar su edad: '))
costo = 5000
resultado = (costo * 0.5)

# Cuerpo

if edad >= 60:
    print (f'Tu edad es {edad} eres mayor de edad,  el costo de la pelicula es {costo}, tu descuento del 50% serian {resultado} ')
else:
    print(f'Tu si tienes que pagar el dinero completo pendejo el costo total es {costo}')