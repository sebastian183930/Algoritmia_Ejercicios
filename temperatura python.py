#NOMBRE: ALGORITMO DE TEMPERATURA

#ENTRADA: ingresar numero para saber si tiene la temperatura adecuada

#SALIDA: ingresar numero para saber si tiene una temperatura adecuada para congelar

#PROCESO: el usuario al ingresar un  numero puede saber si es la temperatura adecuada para congelacion

numero1 =float (input("ingrese la temperatura:"))
if numero1>= 1:
    print ("la temperatura no es suficiente para congelar")
else:
    print ("la temperatura es suficiente para congelar")