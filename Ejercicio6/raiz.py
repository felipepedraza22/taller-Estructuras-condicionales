"""calcular raicess de segundo grado de coeficientes reales"""

# input
a=int(input(" Digite el valor de a:"))
b=int(input(" Digite el valor de b: "))
c=int(input(" digite el valor de c: "))

#processing
d= b*b-4*a*c

if d==0:
    x1= -b/2*a
    x2= -b/2*a
elif d>0:
    x1= (-b+d**0.5)/2*a
    x2= (-b-d**0.5)/2*a
elif d<0:
    x1= ((-b+(1**0.5)*(d**0.5))/2*a)
    x2= ((-b-(1**0.5)*(d**0.5))/2*a)

#output
print("\nResultados\n")
print("x1 es gual a " +str(x1))
print("x2 es igual a " +str(x2))