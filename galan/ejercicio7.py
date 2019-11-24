#Decodificar mensaje encriptado
import os
# D = Buenas tardes
# E = Su nota es 18
# Z = Por lo tanto aprobo el curso
# W = Nos vemos el siguiente ciclo
msg= os.sys.argv[1].upper()

for letra in msg:
    if letra == "D" :
        print("Buenas tardes")
    if letra == "E" :
        print("Su nota es 18")
    if letra == "Z" :
        print("Por lo tanto aprobo el curso")
    if letra == "W" :
        print("Nos vemos el siguiente ciclo")
#fin_iterador

print("fin del bucle")