import os
# declarar variables
estacion = " "

# pedir la variable vía argumento
estacion = os.sys.argv [1]
estacion_invalida = True

# si la estación es invalida volver a pedir la estación
while (estacion_invalida):
    estacion = input ( " Ingrese la estacion (verano / invierno / otoño / primavera): " )
    estacion_invalida = (estacion != "verano"  and estacion !=  " invierno "  and
                          estacion != " otoño "  and estacion != " primavera " )
# fin mientras
print ( " fin del bucle " )
print ( " la estacion es: " , estacion)