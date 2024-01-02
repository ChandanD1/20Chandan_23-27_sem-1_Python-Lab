# Write a program to extend a list in python by using given approach.
# i. By using + operator.
# ii. By using Append ()
# iii. By using extend ()

list = [1, 2, 3]

# i. By using + operator
extend1 = list + [4, 5, 6]
print("i. Extended list using + operator:", extend1)

# ii. By using Append()
list.append(4)
list.append(5)
list.append(6)
print("ii. Extended list using Append():", list)

# iii. By using extend()
list = [1, 2, 3]
list.extend([4, 5, 6])
print("iii. Extended list using extend():", list)
