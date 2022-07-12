# Approach 1: Sort method
mylist = [1,50,3,200,158,16]
mylist.sort()
print("Second Largest Number: ", mylist[-2])

# Approach 2: Using Set
mylist = [1,50,3,200,158,16]
newlist = set(mylist)
newlist.remove(max(newlist))
print(max(newlist))