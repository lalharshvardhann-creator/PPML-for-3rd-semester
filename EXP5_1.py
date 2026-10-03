#WAP to input two dictionaries and print the values by merging the two dictionaries.
d1 = dict(eval(input("Enter first dictionary: ")))
print(d1)
d2 = dict(eval(input("Enter second dictionary: ")))
print(d2)
d1.update(d2)
print("Merged dictionary:", d1)