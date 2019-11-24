#Decodificar mensaje encriptado
import os
# K = Buenos dias
# L = Estan coordinarmente invitados
# O = A mi reunion
# S = El dia de mañana
# X = Gracias
msg= os.sys.argv[1].upper()

for letra in msg:
    if letra == "K" :
        print("Buenos dias")
    if letra == "L" :
        print("Estan coordinarmente invitados")
    if letra == "O" :
        print("A mi reunion")
    if letra == "S" :
        print("El dia de mañana")
    if letra == "X":
        print("Gracias")

#fin_iterador

print("fin del bucle")