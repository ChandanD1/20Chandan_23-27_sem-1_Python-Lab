# Write a program to take input from user for addition of two numbers using
# (single inheritance)

class addition:
    def add(self, a, b):
        return a + b
    
class values(addition):
    def get_input(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        return num1, num2

add_values = values()
numbers = add_values.get_input()
result = add_values.add(*numbers)
print(f"The sum of {numbers[0]} and {numbers[1]} is: {result}")