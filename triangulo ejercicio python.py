#NOMBRE: ALGORITMO DE TRIANGULO

#ENTRADA: ingresar numero 

#SALIDA:  saber si es escaleno  isoceles O equilatero


#PROCESO: este algoritmo lo que hace es que el usuario compruebe cual de los lados pertenece a isosceles equilatero o escaleno



num1=float(input("ingrese el lado 1:"))
num2=float(input("ingrese el lado 2:"))
num3=float(input("ingrese el lado 3:"))
if num1 == num2 and num2 == num3:
    print ("el triangulo es equilatero")
elif num1 == num2 and num2 != num3:
    print ("el triangulo es isoceles")
else:
    print ("el triangulo es escaleno")