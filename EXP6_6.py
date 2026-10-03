# WAP to print the intersection of 2 arrays using lambda function
a1=list(eval(input("Enter the 1st list:")))
a2=list(eval(input("Enter the 2nd list:")))
intersection=list(filter(lambda x: x in a1,a2))
print("Intersection of array1 & array2 is:",intersection)