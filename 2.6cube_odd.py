# Write a program that creates dictionary of cube of odd numbers in the range.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

cube_dict = {num: num ** 3 for num in range(start, end + 1) if num % 2 != 0}

print("Dictionary of Cubes for Odd Numbers:", cube_dict)
