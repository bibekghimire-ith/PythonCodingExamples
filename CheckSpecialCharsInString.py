import re

str1 = "welcome@@2To&&python(#)$$programming"

regex = re.compile('!@#$%^&*(_){}[]<>?|/;')

if(regex.search(str1) == None):
	print("No special chars")
else:
	print("Found special chars")