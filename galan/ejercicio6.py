#Decodificar mensaje encriptado
import os
# A = Hola
# B = Cuando vienes
# C = Te necesito
# D = Chau
msg= os.sys.argv[1].upper()

for letra in msg:
    if letra == "A" :
        print("Hola")
    if letra == "B" :
        print("Cuando vienes")
    if letra == "C" :
        print("Te necesito")
    if letra == "D" :
        print("Chau")
#fin_iterador

print("fin del bucle")