# Maximum and Minimum Elements of an array...

arr = [12, 1, 15,8, 17,9]
maxm = arr[0]
minm = arr[0]

for i in range(len(arr)):
	if arr[i] > maxm:
		maxm = arr[i]
	if arr[i] < minm:
		minm = arr[i]

print("Maximum value is ", maxm)
print("Minimum value is ", minm)

# Using python inbuilt functions...
print(max(arr),min(arr))