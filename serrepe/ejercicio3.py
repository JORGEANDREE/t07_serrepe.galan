import os
#declarar variables
dinero,pu_ticket,nro_tickes=0.0,0.0,0.0

#pedir las variables via argumentos
dinero=float(os.sys.argv[1])
pu_ticket=float(os.sys.argv[2])
nro_tickes=dinero//pu_ticket

#validacion
vale=(nro_tickes>100.0)
dinero_invalido=(dinero<0)
pu_ticket_invalido=(pu_ticket<0)

#while
while(dinero_invalido == True or pu_ticket_invalido == True):
    dinero=float(input("ingrese el dinero:"))
    pu_ticket=float(input("ingres el precio unatario de los tickets:"))
    dinero_invalido = (dinero < 0)
    pu_ticket_invalido = (pu_ticket < 0)
#fin_while

#condicional simple
if(vale==True):
    print("GANASTE UN VALE PARA UN JUEGO MAS")
#fin_if
#impresion
print("#################################")
print("###############JUEGOS############")
print("# Dinero",dinero)
print("# precio unitario del ticket:",pu_ticket)
print("# NRO ticket:",nro_tickes)
print("#################################")