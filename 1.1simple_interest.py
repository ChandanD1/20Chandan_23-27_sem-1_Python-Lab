# Write a program to compute Simple Interest.

principle = int(input("Enter Principle Amount: ₹"))
rate = int(input("Enter Rate Of Interest: "))
time = int(input("Enter Time Period: "))

si = (principle * rate * time) / 100

print("The Simple Interest is:", si)
