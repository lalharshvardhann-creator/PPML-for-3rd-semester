# WAP TO ENTER THREE SIDES OF A TRAINGLE.FOND OUT THE AREA OF TRIANGLE
import math
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3nd number:"))
s=float((a+b+c)/2)
z=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of tringle is:",z)