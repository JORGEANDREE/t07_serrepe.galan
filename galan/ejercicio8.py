#Decodificar mensaje encriptado
import os
# M = Buenas noches
# N = Necesito que me mande su trabajo
# O = Sino no sera evaluado
# P = Gracias
msg= os.sys.argv[1].upper()

for letra in msg:
    if letra == "M" :
        print("Buenas noches")
    if letra == "N" :
        print("Necesito que me mande su trabajo")
    if letra == "O" :
        print("Sino no sera evaluado")
    if letra == "P" :
        print("Gracias")

#fin_iterador

print("fin del bucle")