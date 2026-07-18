#WAP to enter a string and print it in reverse also print the no of vowels and consonant in it.
x = input("Enter a string: ")
print(x[::-1])

v = sum(1 for i in x if i.lower() in 'aeiou')
c = sum(1 for i in x if i.isalpha() and i.lower() not in 'aeiou')

print("Vowels:", v)
print("Consonants:", c)
