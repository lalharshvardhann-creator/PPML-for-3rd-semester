#WAP to create a dictionary and print the key which has the maximum unique value.
d = dict(eval(input("Enter dictionary: ")))
s=[]
s1=[]
for v in d.keys():
    s.append(v)
for b in d.values():
    s1.append(b)
mv=s1[0]
mk=s[0]
for i in range(1,len(s)):
    if s1[i]>mv:
        mv=s1[i]
        mk=s[i]
print("Enter ")