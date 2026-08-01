def fibonacci(n):
    a = 1
    b = 1

    print(a, b, end=" ")

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

n = int(input("Enter the number of terms you want to print: "))

print("The Fibonacci series of first", n, "terms are:")
fibonacci(n)