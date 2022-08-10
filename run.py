import sys
import os
import json

def clear_terminal():
    """
    Function to clear sreen - good for ease of use and read
    """
    os.system('clear')


def display_menu():
    """
    Display menu option to users
    """
    print("*********************************************")
    print("*                                           *")
    print("*           Welcome to Quizeroo             *")
    print("*                                           *")
    print("*********************************************")

    choice = input("""
           1: Play Game
           2: Read Rules
           3: Quit

           Please enter your choice: 
*********************************************
           """)

    if choice == "1":
        clear_terminal()
        play_game()
    elif choice == "2":
        clear_terminal()
        read_rules()
    elif choice == "3":
        # exits the program
        sys.exit("Goodbye, please call again soon!")      
    else:
        print("!!!Please select either 1.(Play Game) or 2. (Read Rules)!!!")
        print()
        menu()


"""
    Display quiz topics for user to choose
"""
def get_quiz_topic():

    print("**********Choose your Quiz Topic*************")
    print()

    choice = input("""
           1: Fr Ted
           2: 80's Pop Music
           3: Geography

           Please enter your choice: 
*********************************************
           """)

    # quiz_topic = input("What quiz topic would you like to choose (A. Fr. Ted, B. 80s Pop Music, or C. Geography): ")
    

"""
    Need to flesh out rules , think about it is there a need to display anything?
"""
def read_rules():
    print("Here's the rules")


"""
    Loops through question bank and prompts user to enter their guess - A, B, C or D
"""
def play_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    get_quiz_topic()

    for question in questions:
        print("-------------------------")
        print("*************************")
        print(question)
        for i in answers[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        # print(guess.upper())
        # if guess.upper() not in ['A', 'B', 'C', 'D']:
        #     print("Please enter A, B, C or D to make your choice")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(question), guess)
        question_num += 1
        # clear_terminal()

    display_score(correct_guesses, guesses)

"""
    Checks answer against guess, returning 1 for correct guesses and 0 for incorrect guesses
"""
def check_answer(answer, guess):

    if answer == guess:
        print("Correct, Well done!")
        return 1
    else:
        print("Incorrect, Hard Luck!")
        return 0


"""
    Display score along with Actual Answers and User Guesses
"""
def display_score(correct_guesses, guesses, answer):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Actual Answers: ", end="")
    for i in answer:
        print(i, end=" ")
    print()

    print("Your Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

"""
    Ask user do they wish to replay game.
"""
def replay_game():

    response = input("Would you like to play again? (Please enter Y (Yes) or N (No): ")
    response = response.upper()

    if response == "YES" or response == "Y":
        return True
    elif response == "NO" or response == "N":
        return True    
    else:
        print("Please enter Y for Yes or N for No")

"""
    Run program functions
"""
# display_menu()

# while replay_game():
#     play_game()

# print("Goodbye, please call again soon!")

# Opening JSON file
f = open('questions_ted.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['question']:
    print(i)

for i in data['options']:
    print(i)    

for i in data['answer']:
    print(i)   
  
# Closing file


# for i in 
# question = (data['question'])

# options = (data['options'])

# answer = (data[ 'answer'])

    guesses = []
    correct_guesses = 0
    question_num = 1

    questions = (data['question'])
    options = (data['options'])
    answer = (data['answer'])

    get_quiz_topic()

    for question in questions:
        print("-------------------------")
        print("*************************")
        print(question)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        # print(guess.upper())
        # if guess.upper() not in ['A', 'B', 'C', 'D']:
        #     print("Please enter A, B, C or D to make your choice")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(answer[question_num-1], guess)
        question_num += 1
        # clear_terminal()

    display_score(correct_guesses, guesses, answer)



f.close()