# Factorial of a number...
# Factorial of 5: 1*2*3*4*5 = 120

# Iterative approach...
num = int(input("Enter a number: "))
fact = 1 
if num < 0:
	print("Factorial does not exist.")
elif num == 0:
	print("Factorial of 0 is 1.")
else:
	for i in range(1,num+1):
		fact = fact*i 
	print("Factorial of ", num, "is ", fact)



# Recursive approach...
def factorial(n):
	# if (n==0 or n==1):
	# 	return 1
	# else:
	# 	return n * factorial(n-1)
	return 1 if (n==0 or n==1) else n*factorial(n-1)

num = 5
print("Factorial of 5: ", factorial(num))