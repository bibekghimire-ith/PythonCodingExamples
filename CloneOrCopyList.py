# Approach 1: Using slicing technique
mylist = [1,2,3,4,5]
list1 = mylist[:]
print(list1)

# Approach 2: Using extend() method
list2 = []
list2.extend(mylist)
print(list2)

# Approach 3: Using the list() method
list3 = list(mylist)
print(list3)

# Approach 4: Using the copy() method
list4 = mylist.copy()
print(list4)

# Approach 5: Using list comprehension
list5 = [i for i in mylist]
print(list5)