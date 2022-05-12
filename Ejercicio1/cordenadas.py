""" Ejercicio1 
Encontrar el cuadrante de las cordenadas"""


from ast import And


print("-----------")
print("---CORDENADAS CARTESIANOS---")
print("--")

# input
X=int(input(" ingrese elvalor de x: "))
Y=int(input(" ingrese el valor de Y: "))

#processing

if X<0 and Y>0:
    print(" esta en el cuadrante 1")
elif X>0 and Y<0:
      print(" esta en el cuadrente 2")
elif X<0 and Y>0:
       print(" esta en el tercer cuadrante")
elif X>0 and Y>0:
      print(" esta en el cuarto cuadrante ")
            


