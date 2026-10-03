#WAP to enter a set and copy the content of the set into a new.set one element at a time.
a = {"apple", "mango", "banana"}
b = set()
for x in a:
    b.add(x)
print("New set:", b)