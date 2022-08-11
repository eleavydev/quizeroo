# list of imports
import sys
import os
import json
import time


def clear_terminal():
    """
    Function to clear sreen - good UX design for ease of reading
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
*           1: Play Game                    *
*           2: Read Rules                   *
*           3: Quit                         *
*                                           *
*           Please enter your choice:       *

*********************************************
           """)

    if choice == "1":
        clear_terminal()
        data = get_quiz_topic_data()
        play_game(data)
    elif choice == "2":
        clear_terminal()
        quiz_rules()
        display_menu()
    elif choice == "3":
        # exits the program
        sys.exit("Goodbye, please call again soon!")
    else:
        clear_terminal()
        print(
            "!Please select either 1: Play Game or 2: Read Rules or 3. Quit!")
        print()
        display_menu()


def get_quiz_topic_data():
    """
    Display quiz topics for user to choose
    """
    print("**********Choose your Quiz Topic*************")
    print()

    choice = input("""
           1: Father Ted
           2: Music
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
        print(
            "!Please select either 1: Father Ted or 2: Music or 3: Geography!")
        get_quiz_topic_data()

    # Opening JSON file
    f = open(filename)

    # returns JSON object as dictionary
    data = json.load(f)

    f.close()

    # Call clear_terminal function to keep screen clean and easy to read
    clear_terminal()

    return data


def quiz_rules():
    """
    Display quiz rules for user
    """
    print("*******************Welcome to Quizeroo!!!******************** ")
    print()
    print("                      Quiz Rules                              ")
    print()
    print("You will have a choice of 3 Quiz Topics to choose from.       ")
    print("""
           1: Father Ted
           2: Music
           3: Geography
           """)
    print("** Each Quiz Topic consists of 5 quick and easy fun questions. ")
    print("** At the end of each quiz topic, your score will be displayed.")
    print("** You can choose to play again if you wish.                  ")
    print()
    print("**************We hope you enjoy Quizeroo!!******************* ")

    input("Please press Enter to continue \n")
    clear_terminal()


def play_game(data):
    """
    Loops through question bank and prompts user to enter - A, B, C or D
    """
    # Populate quiz list variables with data from json files
    questions = (data['questions'])
    options = (data['options'])
    answers = (data['answers'])

    # Initialise other quiz variables as necessary
    guesses = []
    correct_guesses = 0
    question_num = 1

    # Loop through questions and prompt user to enter A, B, C or D
    for question in questions:
        print("*********************************************")
        print(question)
        print()
        for i in options[question_num-1]:
            print(i)
        print()
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        # Call check_answer function and increment correct_guesses variable
        correct_guesses += check_answer(answers[question_num-1], guess)
        question_num += 1
        # Call clear_terminal function to keep screen clean and easy to read
        clear_terminal()
    # Call display_score function passing in necessary quiz variables
    display_score(correct_guesses, guesses, answers, questions)


def check_answer(answer, guess):
    """
    Checks answer against guess, returning 1 for
    correct guesses and 0 for incorrect guesses
    """
    if answer == guess:
        print("Correct, Well done!")
        time.sleep(1)
        return 1
    else:
        print("Incorrect, Hard Luck!")
        time.sleep(1)
        return 0


def display_score(correct_guesses, guesses, answers, questions):
    """
    Display score along with Actual Answers and User Guesses
    """
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    # loop through list of actual answers and print out to screen
    print("Actual Answers: ", end="")
    for i in answers:
        print(i, end=" ")
    print()

    # loop through list of user guesses and print out to screen
    print("Your Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Calculate and print user score out to screen
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def replay_game():
    """
    Ask user do they wish to replay game.
    """
    response = input(
        "Would you like to play again? (Please enter Y (Yes) or N (No): ")
    response = response.upper()

    if response == "YES" or response == "Y":
        return True
    elif response == "NO" or response == "N":
        return False
    else:
        print("Please enter Y for Yes or N for No")
        replay_game()


def main():
    """
    Calls display_menu function which presents users with game options
    From there the main game flow happens
    Once game is finished, the user is asked if they wish to play again
    If they don't wish to Goodbye message is displayed
    """
    display_menu()

    while replay_game():

        data = get_quiz_topic_data()
        play_game(data)

    print("Goodbye, please call again soon!")

main()
