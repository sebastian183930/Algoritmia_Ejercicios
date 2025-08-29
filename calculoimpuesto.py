#NOMBRE: ALGORITMO DE CALCULO IMPUESTO

#ENTRADA: ingresar su salario 

#SALIDA: ingresar su salario para saber si paga impuesto o no
#PROCESO: saber si el salario de la persona paga impuesto o no

salario=float(input("ingrese su salario:"))
if salario > 3000:
    impuesto = salario * 0.15
elif salario > 0:
    impuesto = salario *0.05
else:
     impuesto = 0
     print("el impuesto a pagar es:",impuesto)
