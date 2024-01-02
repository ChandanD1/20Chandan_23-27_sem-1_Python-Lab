# Write a program to compare two dictionaries in Python?
# (By using == operator)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 1, "b": 2, "c": 3}

equal = dict1 == dict2

print("Dictionaries are equal." if equal else "Dictionaries are not equal.")