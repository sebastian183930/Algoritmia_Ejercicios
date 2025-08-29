#nombre: NUMEROS NEGATIVOS
#ENTRADA: INGRESAR NUMERO

#SALIDA: INGRESAR NUMERO PARA COMPROBAR SI EL NUMERO ES NEGATIVO

#PROCESO: AL INGRESAR EL NUMERO EL USURARIO PUEDE SABER SI EL NUMERO ES POSITIVO O NO


#definir si el numero es negativo
numero1= int(input("ingrese un numero:"))
#verificar si el numero es negativo
if numero1 < 0:
    print("el numero es negativo:")
else:
    print("el numero no es negativo:")
