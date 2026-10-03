#WAP to convert all the characters into uppercase and lowercase and eliminate duplicate letter from a given sequence.Use map() function.
def swap(y):
    if y.isupper():
        return y.lower()
    else:
        return y.upper()
y = list(eval(input("Enter the character list: ")))
s = map(swap, y)
print(set(s))