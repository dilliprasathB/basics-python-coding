a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
 
matrix_add=[[a[i][j]+b[i][j]for j in range(len(a[0]))]for i in range(len(a))]
matrix_sub=[[a[i][j]-b[i][j]for j in range(len(a[0]))]for i in range(len(a))]

for row in matrix_add:
    print(row)
for col in matrix_sub:
    print(col)
