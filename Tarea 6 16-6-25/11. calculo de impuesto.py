'''''
Cálculo de impuestos
 Pide al usuario su salario mensual y aplica los siguientes impuestos:
Menos de 10,000: 0%
Entre 10,000 y 30,000: 10%
Más de 30,000: 20%
'''''

# Datos

salario = int(input('Ingrese su salario mensual'))
impuesto1 = (salario * 0.10)
impuesto2 = (salario * 0.20)

# Cuerpo

if salario < 0:
    print ('No te agas es imposible que ganes en numeros negativos')
elif salario < 10000:
    print ('Esta vez no se cobra impuesto')
elif salario >= 10000 and salario <= 30000:
    print (f'El impuesto por cobrar seria {impuesto1}')
else:
    print (f'esta vez el impuesto del 20% serian {impuesto2}')
