# Approach 1: Sort the list in ascending order and print first and last element in list
mylist = [10, 1, 100, 5]
mylist.sort()
print(mylist[0],mylist[-1])


# Approach 2: Using min() and max() method
mylist = [10, 1, 100, 5]
print("Smallest: ", min(mylist))
print("Largest: ", max(mylist))