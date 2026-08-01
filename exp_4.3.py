s = []

x = int(input("Enter the number of elements: "))

for i in range(x):
    n = int(input("Enter the element: "))
    s.append(n)

for i in range(x):
    if s[i] % 2 != 0:
        s[i] = s[i] + 5

print(s)