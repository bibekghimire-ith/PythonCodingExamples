# Approach 1: Looping Method
mylist = [1,2,3,4,5,10,20,30,40,50]
ele = 32

flag = 0
for i in mylist:
	if i==ele:
		flag = 1
		print("Element found...")
		break
if flag==0:
	print("Element not found...")


# Approach 2: Using "in" operator
ele = 10
if ele in mylist:
	print("Element is present...")
else:
	print("Element is not present...")