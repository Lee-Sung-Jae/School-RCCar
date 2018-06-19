import random # Import random library to create random numbers

count = int(input('Input lotto count: '))  # Get input
for i in range(0, count): # for-loop
	print(random.sample(range(1, 46), 6)) # Print random 6 numbers in range 1~45.
