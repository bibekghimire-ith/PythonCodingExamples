# Print Fibonacci Series...
# Each number is sum of preceding two numbers
# 0 1 1 2 3 5 8 13 21

n1 = 0
n2 = 1

fib = [0,1]
n = 10
for i in range(2,n):   # range(3,n+1)
	n1,n2 = n2,n1+n2
	fib.append(n2)
print(fib)
# def fibonacci()	

def recursive(n):
	if n <=1:
		return n
	else:
		return(recursive(n-1)+recursive(n-2))
terms = 10
if terms > 1:
	for i in range(terms):
		print(recursive(i))