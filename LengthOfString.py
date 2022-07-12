# Approach 1: Using for loop
s = "welcome"
counter = 0
for i in s:
	counter += 1
print(counter)

# Approach 2: Using while loop and slicing
counter = 0
while s[counter:]:
	counter += 1
print(counter)

# Approach 3: Using len() built-in function
print(len(s))

# Approach 4: Using join and count
random_str = "X"
print((random_str).join(s).count(random_str)+1)