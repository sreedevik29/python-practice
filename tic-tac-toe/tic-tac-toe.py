theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
			"mid-L": " ", "mid-M": " ", "mid-R": " ",
			"low-L": " ", "low-M": " ", "low-R": " "}

def wholeBoard(board): 
	print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
	print("-+-+-")
	print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
	print("-+-+-")
	print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])

turn = "X"
for i in range(9):
	wholeBoard(theBoard)
	print("Turn for " + turn + ". Move on which space? ")
	move = raw_input()
	theBoard[move] = turn
	if turn == "X":
		turn = "O"
	else:
		turn = "X"

wholeBoard(theBoard)			

# def winner():
# 	if theBoard["top-L"] == "X" and theBoard["top-M"] == "X" and theBoard["top-R"] == "X":
# 		print("Player X won!")
# 	else:
# 		print("No one won. Sorry, try again!")

# winner()