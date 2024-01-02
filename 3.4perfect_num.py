# Write a program to Check whether a number is perfect or not.

def perfectnum(number):
    if number <= 0:
        return False
    divsum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divsum == number
check = int(input("Enter a number: "))
result = perfectnum(check)

if result:
    print(f"{check} is a perfect number.")
else:
    print(f"{check} is not a perfect number.")
