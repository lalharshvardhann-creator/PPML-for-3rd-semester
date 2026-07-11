#WAP TO ENTER THE COEFFICIENTS OF A QUADRATIC EQUATION AND FIND OUT THE ROOTS OF THE EQUIVQLENt.
import math
a=int(input("enter the 1st value for a:"))
b=int(input("enter the 2nd value for b:"))
c=int(input("enter the 3rd value for c:"))
d=math.sqrt(b*b)-(4*a*c)
x=(-b+d)/(2*a)
y=(-b-d)/(2*a)
print("value of x:",x)
print("value of y:",y)