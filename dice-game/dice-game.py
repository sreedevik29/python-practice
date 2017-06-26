#Dice rolling simulator

#Choose number between 1 and 6
#Need a function
#Need a max and min
#Need a random function
 
from random import *

def dice_game():
		
	roll = raw_input("Roll the dices? ")
		
	if roll == "yes" or roll == "y":
		print("Rolling the dice...")
		print("The numbers on the die are: ")
		print randint(1, 6)
		print randint(1, 6) 

	play_again = raw_input("Do you want to play again? ")
	
	if play_again == "yes" or play_again == "y":
		dice_game()
	else:
		print("Thanks for playing!")

def main():
	dice_game()

if __name__ == '__main__':
	main()


