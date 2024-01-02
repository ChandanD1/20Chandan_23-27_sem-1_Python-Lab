# Write a program to find whether given number is an Armstrong Number.

a = int(input("Enter a number: "))

numbers = len(str(a))
sum = 0
temp = a

while temp > 0:
    digit = temp % 10
    sum += digit ** numbers
    temp //= 10

if a == sum:
    print(f"{a} is an Armstrong number.")
else:
    print(f"{a} is not an Armstrong number.")
