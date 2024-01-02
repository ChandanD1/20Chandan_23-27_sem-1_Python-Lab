# Write a program to print 1-22-333-4444-55555 Pattern

n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()