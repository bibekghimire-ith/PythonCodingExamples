# Approach 1: Loop Method / Traversal
mylist = [1,2,3,4,5]
result = 1
for i in mylist:
	result = result * i
print("Product", result)

# Approach 2: Using numpy.prod() method
import numpy

print(numpy.prod(mylist))