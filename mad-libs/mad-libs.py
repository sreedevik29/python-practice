from random import *

def main():
	name = raw_input("Write a name: ")
	favourite_activity = raw_input("Write what your favourite activity is: ")
	emotion = raw_input("Name an emotion: ")
	pet = raw_input("What is your favourite animal? ")
	second_name = raw_input("What would you name a pet: ")
	celebration = raw_input("Name a holiday you'd like to celebrate: ")
	third_name = raw_input("Write a third name: ")
	second_activity = raw_input("Write another activity you like to do: ")
	second_emotion = raw_input("How do you feel about that activity? ")

	print("Hi, my name is " + name + ". My favourite thing to do is " + favourite_activity + ". It makes me feel " + emotion + ". I love my pet " + pet + " whose name is " + second_name + ". Tomorrow is " + celebration + " and to celebrate, my best friend " + third_name + " and I are going to " + second_activity + ". I'm feeling very " + second_emotion + " about tomorrow.")

if __name__ == '__main__':
	main()