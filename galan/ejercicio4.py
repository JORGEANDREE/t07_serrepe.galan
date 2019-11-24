import os
#declarar variables
base,altura,area=0.0,0.0,0.0

#pedir las variables via argumentos
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
area=(base*altura)
area_invalida=(area<10.3 or area>30.5)

#while
while (area_invalida ==True):
    base=float(input("pedir la base:"))
    altura =float(input("pedir la altura:"))
    area = (base * altura)
    area_invalida=(area<10.3 or area>30.5)
#fin_del while
print("fin del bucle")
print("area:",area)