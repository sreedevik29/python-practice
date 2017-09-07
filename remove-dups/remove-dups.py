lists = ["droop", "stoop", "droop", "doop", "loop", "loop", "stoop", "foop"]
newLists = []

def appendList(lists,newLists):
	for i in lists:
		if i not in newLists:
			newLists.append(i)
		print(newLists)

def main():
	appendList(lists,newLists)

if __name__ == '__main__':
	main()
