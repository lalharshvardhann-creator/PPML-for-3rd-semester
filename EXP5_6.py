#WAP to enter two different sets with string elements combine both the sets remove any duplicates are present,print the new set.
set1 = set(input("Enter elements of first set: ").split())
set2 = set(input("Enter elements of second set: ").split())
c = set1|set2
print("New set:", c)