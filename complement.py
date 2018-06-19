inputValue = int(input('Input integer: ')) # Get input
complement = [] # Crete List Variable

for i in range(2, len(str(bin(inputValue)))): # for-loop
	complement.append(str((int(str(bin(inputValue))[i]) == 0) and 1 or 0)) # Get One's Complement

print('Binary: ' + bin(inputValue)[2:]) # Prints binary value, cut first 2 chars to remove '0b'
print('One\'s Complement: ' + ''.join(complement)) # Prints One's Complement
print('Two\'s Complement: ' + '0' + str(bin(int(''.join(complement), 2) + 1))[2:]) # Prints Two's Complement, Make Complement to Integer -> Plus 1 -> Make to Binary -> Cut first 2 chars to remove '0b' -> Make to String
