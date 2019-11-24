import os
# Decodificar mensaje encriptado
# E = FELIZ
# F = CUMPLEAÑOS
# G = :)
# H = !
msg=os.sys.argv[1]
#for
for letra in msg:
    if letra == "E":
        print("FELIZ")
    if letra == "F":
        print("CUMPLEAÑOS")
    if letra == "G":
        print(":)")
    if letra == "H":
        print("!")
#fin_iterador

print("Fin del bucle")
