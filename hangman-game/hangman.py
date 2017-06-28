from random import *

def hangman():
	print("I am thinking of an 8 letter word in NICKNAMES")
	print("Guess a letter!")
	
	user_inputs = [
		{
			"user_input1": raw_input()
		},
		{
			"user_input2": raw_input()
		},
		{
			"user_input3": raw_input()
		},
		{
			"user_input4": raw_input()
		},
		{
			"user_input5": raw_input()
		},
		{
			"user_input6": raw_input()
		},
		{
			"user_input7": raw_input()
		},
		{
			"user_input8": raw_input()
		},
		{
			"user_input9": raw_input()
		}
	]

	if user_inputs == "h":
		print("You guessed a correct letter!")
	elif user_inputs == "o":
		print("You guessed a correct letter!")	
	elif user_inputs == "n":
		print("You guessed a correct letter!")	
	elif user_inputs == "e":
		print("You guessed a correct letter!")	
	elif user_inputs == "y":
		print("You guessed a correct letter!")	
	elif user_inputs == "b":
		print("You guessed a correct letter!")	
	elif user_inputs == "u":
		print("You guessed a correct letter!")	
	elif user_inputs == "n":
		print("You guessed a correct letter!")		
	else:
		print("That's not the right letter!")	

def main():
	hangman()

if __name__ == '__main__':
	main()