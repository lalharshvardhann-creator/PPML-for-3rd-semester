#WAP to enter a number and check wheather it is a palindrome number or not.
x=input("enter number:")
if x==x[::-1]:
    print("palindrom")
else:
    print("not plindrom")
