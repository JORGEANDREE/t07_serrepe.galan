import os
# Mostrar mensaje "Desea consegir trabajo?" si o no ?
#declarar variables
rpta=""
#pedir la variable via argumento
rpta=os.sys.argv[1]
#condicion
rpta_invalida=True
#si la respues es invalida pedir denuevo el msj
while(rpta_invalida):
    rpta=input("Desea conseguir trabajo ? (si/no): ")
    rpta_invalida=(rpta != "si" and rpta != "no")
#fin_while
print("Fin del bucle")
print("La respuesta es :", rpta)
