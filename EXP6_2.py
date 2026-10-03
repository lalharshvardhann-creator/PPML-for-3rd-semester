#WAP yo print a matrix along eith a summation of row elemants and column elements after entering a 3*3 matrix.
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, " "]] 
rows = len(a) 
cols = len(a[0]) 
for i in range(0, rows): 
    sumRow = 0 
for j in range(0, cols): 
    sumRow = sumRow + a[i][j] 
b[i][j] = a[i][j] 
b[i][cols] = sumRow 
for i in range(0, cols): 
    sumCol = 0 
for j in range(0, rows): 
    sumCol = sumCol + a[j][i] 
    b[rows][i] = sumCol 
for i in range(0,rows+1): 
    for j in range(0,cols+1): 
        print(b[i][j],"\t",end=" ")
    print()