# Working with % operator (checks if there's a remained when dividing)

num = input("Enter a number: ")
mod = num % 2 # checks if it's divisible by 2

if mod > 0: # if there is a or remainder is greater than 0
	print("You picked an odd number!")
else: # it's divisible by 2 so there's no remainder
	print("You picked an even number!")