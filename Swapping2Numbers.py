# Swapping 2 numbers...

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

# Approach 1...
temp = num1
num1 = num2
num2= temp

print(num1,num2)

# Approach 2...
num1,num2 = num2, num1
print(num1,num2)