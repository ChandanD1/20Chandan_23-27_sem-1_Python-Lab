# Write a program to add two matrices.

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix: ")

matrix1= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix1:
    print(n)

print("Enter the elements of Second Matrix:")
matrix2= [[int(input()) for i in range(column)] for i in range(rows)]
for n in matrix2:
    print(n)
    
result=[[0 for i in range(column)] for i in range(rows)]

for i in range(rows):
    for j in range(column):
        result[i][j] = matrix1[i][j]+matrix2[i][j]

print("The Sum of Above two Matrices is : ")
for r in result:
    print(r)