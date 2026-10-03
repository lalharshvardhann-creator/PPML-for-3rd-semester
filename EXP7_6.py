#WAP to find the ratio of positive numbers, negative numbers and zeroes in an array of integers using map(). 
x = list(eval(input("Enter the integer array: ")))
print("The original list:", x)
pos = list(filter(lambda y: y > 0, x))
zero = list(filter(lambda y: y == 0, x))
neg = list(filter(lambda y: y < 0, x))
n = len(x)
z1 = [
    round(len(pos) / n, 2),
    round(len(neg) / n, 2),
    round(len(zero) / n, 2)
]
def ratio(x):
    return x
l1 = list(map(ratio, z1))
print("The ratio array:", l1)