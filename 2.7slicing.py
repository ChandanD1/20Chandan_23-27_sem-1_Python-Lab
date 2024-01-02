# Write a program for various list slicing operation.

# List
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i. Print  list
print("i. List:", a)

# ii. Print 4th element of list
print("ii. 4th element of list:", a[3])

# iii. Print list from 0th to 4th index
print("iii. List from 0th to 4th index:", a[:5])

# iv. Print list -7th to 3rd element
print("iv. List from -7th to 3rd element:", a[-7:3])

# v. Appending an element to list
a.append(110)
print("v. List after appending 110:", a)

# vi. Sorting the elements of list
a.sort()
print("vi. Sorted list:", a)

# vii. Popping an element
popped_element = a.pop()
print("vii. Popped element:", popped_element, "Updated list:", a)

# viii. Removing specified element
a.remove(60)
print("viii. List after removing 60:", a)

# ix. Entering an element at specified index
a.insert(2, 35)
print("ix. List after inserting 35 at index 2:", a)

# x. Counting the occurrence of a specified element
count_30 = a.count(30)
print("x. Occurrence of 30 in the list:", count_30)

# xi. Extending list
a.extend([120, 130])
print("xi. Extended list:", a)

# xii. Reversing the list
a.reverse()
print("xii. Reversed list:", a)
