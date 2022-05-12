"""Ejercicio de prestamo:"""

print("-----")
print("---valor de ingresos---")
print("----")

#input 
Ingresos=int(input(" ingrese el numero de sus ingresos "))
deudas=int(input(" ponga 0 si no tiene deudas o ponga 1 si tiene deudas "))

# processing 
if deudas==0 and Ingresos>945200:
    print(" aprobado el prestamo ")
elif deudas>0 and Ingresos<945200:
    print(" no puede ser aprobado ")
