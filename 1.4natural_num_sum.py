# Write a program to print first n natural number & their sum.

n = int(input ("Enter a Number: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print ("The sum is: ", sum)
