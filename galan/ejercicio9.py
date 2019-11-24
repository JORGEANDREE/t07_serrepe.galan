#Decodificar mensaje encriptado
import os
# H = Hola
# I = Quisiera saber
# G = Si hoy hay tarea
# J = Porfavor
# T = Gracias
msg= os.sys.argv[1].upper()

for letra in msg:
    if letra == "H" :
        print("Hola")
    if letra == "I" :
        print("Quisiera saber")
    if letra == "G" :
        print("Si hoy hay tarea")
    if letra == "J" :
        print("Porfavor")
    if letra == "T":
        print("Gracias")
#fin_iterador

print("fin del bucle")