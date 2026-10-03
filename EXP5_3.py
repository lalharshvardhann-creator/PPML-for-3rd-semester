#WAP to enter a dictionary and remove the duplicate value inside the dictionary.
d = {"a": 10, "b": 20, "c": 10, "d": 30}
new = {}
for key in d:
    if d[key] not in new.values():
        new[key] = d[key]
print("New dictionary:", new)
