# Write a program to create a list of tuples from given list having number and add its cube in tuple.
# i/p: c= [2,3,4,5,6,7,8,9]

numbers = [int(n) for n in input("Enter numbers separated by spaces: ").split()]

cubes_tuples = [(num, num ** 3) for num in numbers]

print("List of tuples giving cube for num:", cubes_tuples)

