#WAP to print the transpose of a matrix of n*n order.
Rows = int(input("Give the number of rows: "))
Columns = int(input("Give the number of columns: "))
matrix = [[int(input()) for c in range(Columns)] for r in range(Rows)]
print("Original Matrix")
for i in range(Rows):
    for j in range(Columns):
        print(matrix[i][j], "\t", end="")
    print()
print("Matrix after transpose")
for i in range(Columns):
    for j in range(Rows):
        print(matrix[j][i], "\t", end="")
    print()