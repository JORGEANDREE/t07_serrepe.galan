import os
# declarar variables
nota1, nota2, nota3, promedio = 0.0 , 0.0 , 0.0 , 0.0

# pedir las variables a través de argumentos
nota1 = float (os.sys.argv [ 1 ])
nota2 = float (os.sys.argv [ 2 ])
nota3 = float (os.sys.argv [ 3 ])
promedio = (nota1 + nota2 + nota3) / 3
promedio_invalido = (promedio < 0  o promedio > 20 )

# while
while (promedio_invalido ==  True ):
    nota1 = float ( input ( " pedir la nota1: " ))
    nota2 = float ( input ( " pedir la nota2: " ))
    nota3 =  float ( input ( " pedir la nota3: " ))
    promedio = (nota1 + nota2 + nota3) / 3
    promedio_invalido = (promedio <  0  o promedio >  20 )
# fin_del while
print ( " fin del bucle " )
print ( " promedio: " , promedio)
