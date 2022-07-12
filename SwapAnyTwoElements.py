# Approach 1: Simple Swap
mylist = [1,2,3,4,5]
pos1 = 1
pos2 = 3

print(mylist)
mylist[pos1],mylist[pos2] = mylist[pos2],mylist[pos1]
print(mylist)


# Approach 2: Using Inbuilt list.pop() function

# Approach 3: Using Tuples