#NOMBRE:ALGORITMO ACCESO

#ENTRADA: ingresar rol 


#SALIDA: ingresar rol si es admin o usuario y mirar si tiene acceso

#PROCESO: el usuario al meter su rol sabra  si tiene acceso o no

rol=str(input("ngrese su rol admid/usuario:"))
if rol == "admin":
    print("acceso permitido")
else:
    print("acceso denegado")
