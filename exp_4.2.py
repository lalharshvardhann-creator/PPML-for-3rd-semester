list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]

s = []

for i in range(len(list1)):
    s.append(str(list1[i]))
    s.append(list2[i])

print(s)