# Prime Numbers...
# Natural no. greater than 1
# Has only two factors: 1 and itself

num = int(input("Enter a number: "))
count = 0

if num > 1:
	for i in range(1,num+1):
		if(num%i) == 0:
			count += 1

	if count==2:
		print(f"{num} is a prime number.")
	else:
		print(f"{num} is not a prime number.")
