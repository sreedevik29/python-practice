# Practice 1

# This program says hello and asks for my name
# Working version:
# print("Hello world")
# myName = raw_input("What is your name? ")
# print("It's good to meet you, " + myName)
# print("The length of your name is: ")
# print(len(myName))
# myAge = raw_input("What is your age? ")
# print("You will be " + str(int(myAge) + 1) + " in a year.")

# Textbook version (Python 3 version):
# print("Hello world!")
# print("What is your name?")
# myName = input()
# print("It's good to meet you, " + myName)
# print("The length of your name is: ")
# print(len(myName))
# print("What is your age?")
# myAge = input()
# print("You will be " + str(int(myAge) + 1) + " in a year.")

# How to use 'len' function to figure out the length of the string
# print(len("Hello there!"))

# How to use 'str' function to change integer into a string
# print("I am " + str(29) + " years old")

# How to use the 'int' function
# print(20 + int('40') + 40)

# How to use the 'float' function for decimals
# print(float(29.9293))

# name = input("Type name: ")
# if name == "Mary":
# 	print("Hello Mary")
# 	password = input("Type password: ")
# 	if password == "swordfish":
# 		print("Access granted")
# 	else:
# 		print("Wrong password. Try again, Mary!")
# else:
# 	print("Yeah, nice try. You're not Mary!")

# name = "Sree"
# age = 2001

# if name == "Alice":
# 	print("Hi, Alice")
# elif age < 12:
# 	print("You are not Alice, kiddo.")
# elif age > 100:
# 	print("You're not Alice, grannie.")
# elif age > 2000:
# 	print("Unlike you, Alice is not an immortal vampire.")
# else: 
# 	print("I don't even know what you are.")

# Goal: To get to B
# 1: F, 2:: T, 3: ?, 4: ?, 

# ...PRE CODE...

# 1. IF --> T/F
# 	A
# 2. ELIF --> T/F
# 	B
# 3. ELIF --> T/F
# 	C
# 4. ELIF --> T/F
# 	C
# ELSE
# 	E

# ...POST CODE...

# While loop examples
# spam = 0
# while spam < 5:
# 	print("Hello world!")
# 	spam = spam + 1

# name = ""
# while name != "Your name":
# 	print("Please type your name.")
# 	name = input()
# print("Thank you.")

# Break statements
# name = "Sreedevi"
# while True:
# 	print("Please type your name.")
# 	name = input()
# 	if name == "Your name":
# 		break
# print("Thank you!")

# Continue statements
# name = "Joey"
# password = "swordfish"
# while True:
# 	print("Who are you?")
# 	name = input()
# 	if name != "Joe":
# 		continue
# 	print("Hello, Joe. What is the password? (It is a fish.)")
# 	password = input()
# 	if password == "swordfish":
# 		break
# print("Access granted")

# For loops and range() function
# print("My name is")
# for i in range(5):
# 	print("Jimmy Five Times (" + str(i) + ")")

#Add all numbers from 0 to 100
# total = 0
# for num in range(101):
# 	total = total + num
# print(total)

#An equivalent while Loop
# print("My name is ")
# i = 0 
# while 1 < 5:
# 	print("Jimmy Five Times (" + str(i) + ")")
# 	i = i + 1

#More on ranges
# for i in range(-2, 5):
# 	print(i)

#Importing:
# import random
# for i in range(5):
# 	print(random.randint(1, 10))

# import sys
# while True:
# 	print("Type exit to exit.")
# 	response = input()
# 	if response == "exit":
# 		sys.exit()
# 	print("You typed " + response + ".")

# A Loop or If statement (conditionals) ONLY runs if the
# condition is True

# number = input("GIVE A NUMBER: ")
# while number > 1:

# Functions
# def hello(name):
# 	print("Hello " + name)
# hello("Alice")
# hello("Bob")

# Global vs. local
# def spam():
# 	global eggs
# 	eggs = "spam"

# def bacon():
# 	eggs = "bacon"

# def ham():
# 	print(eggs)

# eggs = 42
# spam()
# print(eggs)

# Handling errors
# def spam(divideBy):
# 	try:
# 		return 42/divideBy
# 	except ZeroDivisionError:
# 		print("Error: Invalid Argument.")
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# loops to enter names
# catNames = []
# while True:
# 	print("Enter the name of cat " + str(len(catNames) + 1) + " (Or enter nothing to stop.): ")
# 	name = raw_input()
# 	if name == "":
# 		break
# 	catNames = catNames + [name] #list concantenation
# print("The cat names are: ")
# for cats in catNames:
# 	print(cats)

# ranges


