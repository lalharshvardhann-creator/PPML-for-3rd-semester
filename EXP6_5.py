# WAP to print Fibonacci series up to n terms using lambda function
n = int(input("Enter the number of terms: "))
Fibonacci = lambda n: [0] if n == 1 else [0, 1] if n == 2 else Fibonacci(n - 1) + [Fibonacci(n - 1)[-1] + Fibonacci(n - 2)[-1]]
print("Fibonacci series:")
for i in range(n):
    print(Fibonacci(i + 1)[-1], end=" ")