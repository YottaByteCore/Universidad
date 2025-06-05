'''''
Escribe un programa que pida al usuario ingresar una contraseña y repita la solicitud mientras la contraseña ingresada sea incorrecta. 
El programa debe continuar hasta que el usuario ingrese la contraseña correcta. Utiliza una estructura whilepara simular un do while.
'''''

# Este programa pide al usuario que escriba una contraseña
# y sigue pidiéndola hasta que escriba la correcta

# La contraseña correcta es esta
contrasena_correcta = "python123"

# Variable para guardar lo que escriba el usuario
contrasena_ingresada = ""

# Simulamos un do-while con un while True
while True:
    contrasena_ingresada = input("Escribe la contraseña: ")
    
    if contrasena_ingresada == contrasena_correcta:
        print("¡Bien! Contraseña correcta.")
        break  # Salimos del bucle si acierta
    else:
        print("Esa no es la contraseña. Intenta otra vez.")

