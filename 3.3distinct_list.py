# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def getelements(list):
    distinctlist = []
    
    for element in list:
        if element not in distinctlist:
            distinctlist.append(element)
    return distinctlist

a = input("Enter elements for list: ")
userlist = a.split()

userlist = [int(element) for element in userlist]

result = getelements(userlist)
print("List:", userlist)
print("List with distinct elements:", result)
