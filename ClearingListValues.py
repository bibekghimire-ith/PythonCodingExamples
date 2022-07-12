# Approach 1: clear()
mylist = [1,2,3,4,5]
print(mylist)
mylist.clear()
print(mylist)

# Approach 2: Initialize the list with no value
mylist = [1,2,3,4,5]
print(mylist)
mylist = []
print(mylist)

# Approach 3: *=0
mylist = [1,2,3,4,5]
print(mylist)
mylist *= 0
print(mylist)

# Approach 4: del()
mylist = [1,2,3,4,5]
print(mylist)
del mylist[:]
print(mylist)