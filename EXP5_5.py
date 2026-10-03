# WAP to enter two sets and perform all the set operations on it.
a = set(input("Enter first set: ").split())
b = set(input("Enter second set: ").split())
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", b - a)
print("Symmetric Difference:", a ^ b)