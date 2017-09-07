

# def appendList(lists,newLists):
# 	for i in lists:
# 		if i not in newLists:
# 			newLists.append(i)
# 		print(newLists)

# def main():
# 	appendList(lists,newLists)

def setList():
	a = ["droop", "stoop", "droop", "doop", "loop", "loop", "stoop", "foop"]
	c = list(set(a))
	print(c)

def main():
	setList()

if __name__ == '__main__':
	main()
