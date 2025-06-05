'''''
 Escribe un programa que pida al usuario que ingrese un número entero positivo. 
 El programa debe mostrar todos los números del 1 hasta el número ingresado, uno por uno, utilizando un bucle while.
 '''''
 # Datos

numero = int(input('Ingresar un numero positivo: '))

# Verificar que el número sea positivo

if numero  <= 0:
    print('Debes ingresar un numero entero positivo')
else:

 # El contador

 i = 1

# bucle

while i <= numero:
    print (i)

    i += 1