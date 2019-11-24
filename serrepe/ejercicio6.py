import os
# Decodificar mensaje encriptado
# A = HELLO
# B = MUNDO
# C = COMO ESTAN
# D = !!!
msg=os.sys.argv[1]
#for
for letra in msg:
    if letra == "A":
        print("HELLO")
    if letra == "B":
        print("MUNDO")
    if letra == "C":
        print("COMO ESTAN")
    if letra == "D":
        print("!!!!")
#fin_iterador

print("Fin del bucle")
