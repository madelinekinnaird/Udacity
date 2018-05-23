"""
Quiz version: A lsit of all prompts and their respective answers are in quiz version.
Heirarchy is "level", either "choose_answers" or "choose_questions", and lastly "index" 
 """

quiz_version = [
["I am not throwing away my (__1__). \n I'm just like my (__2__),\n I'm (__3__),\n scrappy, and (__4__).",["shot", "country", "young", "hungry"]],
["You will come of age with our young (__1__). \n  We'll (__2__) and (__3__) for you.\n We'll make it (__4__) for you.",["nation", "bleed", "fight", "right"]],
["Let me tell you what I wish I'd known, \n when I was young a dreamed of (__1__)\n you have no (__2__) \n who (__3__), who dies, \n who tells your (__4__).",["glory", "control", "lives", "story"]]
]

choose_questions = 0 #identifier to assist in categorizing the list of quiz version. Basically using this will point the program to the questions.
choose_answers = 1 #identifier to assist in categorizing the list of quiz version. Basically using this will point the program to the answers.


"""
level_choice: Asks user for Hamilton character or "level".
INPUT: user inputs data into user_level_choice
OUTPUT: returns a numeric value that corresponds to level
"""

def level_choice():
	user_level_choice = (raw_input("Which character from Hamilton would you like to rap? \n Hamilton? \n Burr? \n Washington?").lower()) #turns all input into lowercase to accept answer regardless of case
	if user_level_choice == "hamilton":
		return 0
	if user_level_choice == "burr":
		return 1
	if user_level_choice == "washington":
		return 2
	

"""
Show questions: function to read out the appropriate prompt or questions
INPUT: level
OUTPUT: prints appropriate prompt or question based on level
"""

def show_questions(level):
	print quiz_version[level][choose_questions] #choose_questions = 0 to indicate correct placement in quiz_version list

"""
check_answers: function to iterate through the 4 blanks per prompt and test if input is correct
INPUT: level and prompt user to input their guess into user_attempt
OUTPUT: prints correct or incorrect per each blank.
"""

def check_answers(level):
	index = 0
	while index < len(quiz_version[level][choose_answers]):#choose_answers = 0 to indicate correct placement in quiz_version list
		blank_number = index + 1 #Added the plus one because I want list ot start at (__1__), rather than (__0__)
		user_attempt = (raw_input("What is the missing word for (__%d__)?" %blank_number).lower())
		if user_attempt == quiz_version[level][choose_answers][index]:
			print"Correct!"
			index = index + 1
		else:
			print "Try again..."
			index = index

"""
game_procedures: function that gives process flow to each other function
first runs level_choice to determine the level, then based off of the level will show the user the question, and check answers
"""

def game_procedures():
	level = level_choice()
	show_questions(level)
	check_answers(level)



print game_procedures()




	

