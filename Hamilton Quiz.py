# Quiz version: A dictionary of all prompts and their respective answers are in quiz version.


quiz_version = {
	'hamilton': {
		'quiz': "I am not throwing away my (__1__). \n I'm just like my (__2__),\n I'm (__3__),\n scrappy, and (__4__).",
		'answers': ["shot", "country", "young", "hungry"]
		},
	'burr': {
		'quiz': "You will come of age with our young (__1__). \n  We'll (__2__) and (__3__) for you.\n We'll make it (__4__) for you.",
		'answers': ["nation", "bleed", "fight", "right"]
		},
	'washington': {
		'quiz': "Let me tell you what I wish I'd known, \n when I was young a dreamed of (__1__)\n you have no (__2__) \n who (__3__), who dies, \n who tells your (__4__).",
		 'answers': ["glory", "control", "lives", "story"]
		 }
	}


# level_choice: Asks user for Hamilton character or "level".
# INPUT: user inputs data into user_level_choice
# OUTPUT: prints the question prompt


def level_choice():
	user_level_choice = raw_input("Which character from Hamilton would you like to rap? \n Hamilton? \n Burr? \n Washington?") #turns all input into lowercase to accept answer regardless of case
	print quiz_version[user_level_choice]['quiz']
	return user_level_choice


# check_answers: function to iterate through the 4 blanks per prompt and test if input is correct
# INPUT: level and prompt user to input their guess into user_attempt
# OUTPUT: returns correct or incorrect per each blank.


def check_answers(user_level_choice):
	answer_index = 0
	
	while answer_index < len(quiz_version[user_level_choice]['answers']):#choose_answers = 0 to indicate correct placement in quiz_version list
		blank_number = answer_index + 1 #Added the plus one because I want list ot start at (__1__), rather than (__0__)
		user_attempt = raw_input("What is the missing word for (__%d__)?" %blank_number)
		if user_attempt == quiz_version[user_level_choice]['answers'][answer_index]:
			print"Correct!"
			replace_questions(user_level_choice, answer_index)
			answer_index = answer_index + 1
		else:
			print "Try again..."
			answer_index = answer_index
			
#replace_question reprints the prompt and fills in the blank as they are answered correctly
#INPUTS: User_level_choice, answer_index, blank_number

def replace_questions(user_level_choice, answer_index):
	blank_index = 0 #index to iterate through the blanks in the prompt
	blank_number_reprint = blank_index + 1 #index to iterate through the (__#'s__) 
	reprint_question = quiz_version[user_level_choice]['quiz'] #initializes the prompt to the original question
	while blank_index <= answer_index:
		replace_answer = str(quiz_version[user_level_choice]['answers'][blank_index]) #turns corresponding answer into a string
		replace_blank = str("(__%d__)" %blank_number_reprint) # turns the blank # into a string
		reprint_question = reprint_question.replace(replace_blank, replace_answer)
		blank_index = blank_index + 1
		blank_number_reprint = blank_number_reprint + 1
	print reprint_question 


# game_procedures: function that gives process flow to each other function
# first runs level_choice to determine the level, then based off of the level will show the user the question, and check answers


def game_procedures():
	user_level_choice = level_choice()
	check_answers(user_level_choice)
	


print game_procedures()





	






	

