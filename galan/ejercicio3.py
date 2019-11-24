import os
#declarar variables
color=""

#pedir la variable via argumento
color=os.sys.argv[1]
color_invalido=True

#si el color es invalido volver a pedir el color
while(color_invalido):
    color=input("Ingrese el color (violeta/rojo/verde/amarillo/morado):")
    color_invalido=(color != "violeta" and color != "rojo" and
                       color !="verde" and color !="amarillo" and color !="morado")
#fin while
print("fin del bucle")
print("el color es:",color)