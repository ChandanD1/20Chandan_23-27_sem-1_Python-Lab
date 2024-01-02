# Write a Python function that accepts a string and counts the number of upper and lower-case letters.
# string_test = 'Today is My Best Day'. 

def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    
    return upper_count, lower_count

test = input("Enter a string: ")
upper, lower = count(test)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
