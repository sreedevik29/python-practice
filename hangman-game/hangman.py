from random import *

def hangman():
	# going = True

	# while going:
	#     prompt = raw_input("Should I keep going? y/n: ")
	#     if prompt == "y":
	#         print("Okay ill keep going...")
	#     else:
	#         print("Okay ill stop.")
	#         going = False

	print("I am thinking of an 8 letter word in NICKNAMES")
	active = True
	word = ["h", "o", "n", "e", "y", "b", "u", "n"]
	# word = [ 
	# 	{
	# 	"h", "o", "n", "e", "y", "b", "u"
	# 	},
	# 	{
	# 	"y", "o", "u", "s", "h", "i", "t", "e", "r"
	# 	}
	# ]
	# select_word = random.choice(word)

	while active:
		user_input = raw_input("Guess the letter: ")
		if user_input in word:
			print("You guessed the right letter")
			while user_input in word:
				word.remove(user_input)
		else: 
			print("You guessed the wrong letter, try again")
		if len(word) == 0:
			print("Congrats you won! The word was honeybun!")
			active = False

	print("Game is over!")


def main():
	hangman()

if __name__ == '__main__':
	main()