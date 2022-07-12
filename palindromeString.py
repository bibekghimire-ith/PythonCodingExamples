# Approach 1: Reverse string and check if reverse is equal to original string
s = input("Enter string: ")

rev = s[::-1]
if rev == s:
	print("String is palindrome")
else:
	print("String is not palindrome")

	