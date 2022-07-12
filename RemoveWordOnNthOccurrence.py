mylist = ['geeks','for','geeks','freak','geeks','freak']
word = 'geeks'
n = 2

count=0
print(mylist)
for i in range(0,len(mylist)-1):
	if mylist[i] == word:
		count+=1
		if count == n:
			del mylist[i]
print(mylist)