import os
#pedir en que dia de la semana estamos
# declarar la variable
dia=""
#pedir la variable via argumentos
dia=os.sys.argv[1]
dia_invalido=True
#si el dia es invalido volver a pedir el dia de la semana
while(dia_invalido):
    dia=input("Ingrese el dia de la semana: (lunes/martes/miercoles/jueves/viernes/sabado/domingo): ")
    dia_invalido=(dia != "lunes" and dia != "martes" and
                   dia != "miercoles" and dia != "jueves" and
                   dia != "viernes" and dia != "sabado" and
                   dia != "domingo")
#fin_while
print("Fin del bucle")
print("el dia es :", dia)
