import sys
import os
import json

# def clear_terminal():
#     """
#     Function to clear sreen - good for ease of reading, accessibility and UX design
#     """
#     os.system('clear')


def display_menu():
    """
    Display menu option to users - allow them enter 1, 2 or 3
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
        # clear_terminal()
        data = get_quiz_topic_data()
        play_game(data)
    elif choice == "2":
        # clear_terminal()
        read_rules()
    elif choice == "3":
        # exits the program
        sys.exit("Goodbye, please call again soon!")      
    else:
        print("!!!Please select either 1.(Play Game) or 2. (Read Rules)!!!")
        print()
        display_menu()


"""
    Display quiz topics for user to choose
"""
def get_quiz_topic_data():

    print("**********Choose your Quiz Topic*************")
    print()

    choice = input("""
           1: Fr Ted
           2: 80's Pop Music
           3: Geography

           Please enter your choice: 
*********************************************
           """)

    # return choice
    if choice == '1':
        filename = "questions_ted.json"
    elif choice == '2':
        filename = "questions_music.json"
    elif choice == '3':  
        filename = "questions_geo.json"
    else:
        print("wrong choice")  

    # Opening JSON file
    # f = open('questions_ted.json')
    f = open(filename)
  
    # returns JSON object as dictionary
    data = json.load(f)

    # for i in data['question']:
    #     print(i)

    # for i in data['options']:
    #     print(i)    

    # for i in data['answer']:
    #     print(i)   

    return data

    # quiz_topic = input("What quiz topic would you like to choose (A. Fr. Ted, B. 80s Pop Music, or C. Geography): ")
    

"""
    Need to flesh out rules , think about it is there a need to display anything?
"""
def read_rules():
    print("Here's the rules")


"""
    Loops through question bank and prompts user to enter their guess - A, B, C or D
"""
def play_game(data):

    guesses = []
    correct_guesses = 0
    question_num = 1

    print("returning quiz topic")
    # print(get_quiz_topic())
    
    questions = (data['questions'])
    options = (data['options'])
    answers = (data['answers'])

    print(questions)
    print(options)
    print(answers)

    for question in questions:
        print("-------------------------")
        print("*************************")
        print(question)
        for i in options[question_num-1]:
            # print("/n")
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        # print(guess.upper())
        # if guess.upper() not in ['A', 'B', 'C', 'D']:
        #     print("Please enter A, B, C or D to make your choice")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(answers[question_num-1], guess)
        question_num += 1
        # clear_terminal()

    display_score(correct_guesses, guesses,answers, questions)

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
def display_score(correct_guesses, guesses, answers, questions):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Actual Answers: ", end="")
    for i in answers:
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


print("elaine")


def main():
    """
    Run all program functions
    """
    display_menu()
    print("elaine")

    # # data = get_quiz_topic_data()
    
    # while replay_game():

    #     data = get_quiz_topic_data()
    #     play_game(data)
    #     # play_game()

    # print("Goodbye, please call again soon!")

# f.close()  - do i need to call this to safely close json file?

main()