# Dice game using a while loop instead of recursion:

from random import *

def dice_game():
		
	user_input = raw_input("Roll the dices? (y/n) ")
		
	while user_input == "yes" or user_input == "y":
		print("Rolling the dice...")
		print("The numbers on the die are: ")
		print randint(1, 6)
		print randint(1, 6) 
		user_input = raw_input("Do you want to play again? (y/n) ")
	
	print("Thanks for playing!")

def main():
	dice_game()

if __name__ == '__main__':
	main()


