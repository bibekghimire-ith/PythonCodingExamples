# swapFirstLastElementOfArray
mylist = [1,2,3,4,5]

# Approach 1: Temp Variable method
temp = mylist[0]
mylist[0] = mylist[len(mylist)-1] 
mylist[len(mylist)-1] = temp

print(mylist)

# Approach 2
mylist = [1,2,3,4,5]
mylist[0],mylist[-1] = mylist[-1],mylist[0]

print(mylist)

# Approach 3: Using Tuple
mylist = [1,2,3,4,5]
get = (mylist[-1],mylist[0]) # Packing in tuple
mylist[0],mylist[-1] = get

print(mylist)

# Approach 4: * operand
mylist = [1,2,3,4,5]
start, *middle, end = mylist
mylist = [end, *middle, start]

print(mylist)

# Approach 5: Pop method
mylist = [1,2,3,4,5]
start = mylist.pop(0)
end = mylist.pop(-1)
mylist.insert(0,end)
mylist.append(start)

print(mylist)
