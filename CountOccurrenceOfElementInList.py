# Approach 1: Loop Method
mylist = [1,2,10,5,10,3,2,10,9,6]
x = 10

count = 0
for i in mylist:
	if i == x:
		count+=1
print(count)

# Approach 2: Using count()
print(mylist.count(x))

# Approach 3: Using counter()
from collections import Counter
dic = Counter(mylist)
print(dic[x])