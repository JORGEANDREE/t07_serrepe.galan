import os
#declarar variables
seccion=""
#pedir la variable via argumento
seccion=os.sys.argv[1]
seccion_invalida=True

#si la seccion es invalida volver a pedir la seccion
while(seccion_invalida):
    seccion=input("Ingrese la seccion (A/B/C/D/E):")
    seccion_invalida=(seccion != "A" and seccion != "B" and
                       seccion !="C" and seccion !="D" and seccion !="E")
#fin while
print("fin del bucle")
print("la seccion es:",seccion)