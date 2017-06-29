from random import *

def hangman():
	print("I am thinking of an 8 letter word in NICKNAMES")
	active = True
	word = "honeybun"

	while active:
		user_input = raw_input("Guess the letter: ")
		if user_input == "h": 
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter!")
		elif user_input == "o":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "n":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "e":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "y":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "b":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "u":
			print("You guessed a correct letter!")
			user_input = raw_input("Guess another letter: ")
		elif user_input == "n":
			print("You guessed a correct letter: ")
			active = False

	print("Game is over")
	# user_input = raw_input("Guess a letter!")

# 	def game_logic():
# 		if user_input == "h" or user_input == "o" or user_input == "n" or user_input == "e" or user_input == "y" or user_input == "b" or user_input == "u" or user_input == "n":
# 			print("You guessed the right word!")
# 		else: 
# 			print("You guessed the wrong word, guess again")

# 	if game_logic() = True:
# 		print("You got the word! It was " + honeybun)
# 	else:
# 		print("You lost")

def main():
	hangman()

if __name__ == '__main__':
	main()