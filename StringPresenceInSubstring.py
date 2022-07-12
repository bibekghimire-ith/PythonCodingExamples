# Using find() method
# find() method returns the index of first occurrence of specified value else -1
s = "welcome to python programming"
sub_str = "python"

print(str.find(sub_str))

if (str.find(sub_str) == -1):
	print("Not Found...")
else:
	print("Found...")