import sys

# Question bank 
# Need to move to questions.py 
frted_questions = {
 "What actor played the role of Father Ted?: ": "A",
 "Who is Ted's nemesis?: ": "D",
 "Who is the priest who comes to stay with Ted and Dougal and is soooooo boring?: ": "B",
 "What's the name of 'The Dancing Priest?: ": "C",
 "Where is the Annual Ted Fest held?: ": "A"
}

frted_answers = [["A. Dermot Morgan", "B. Donald Trump", "C. Niall Horan", "D. Ardal O Hanlon"],
          ["A. Father Jack Hackett", "B. Father Brian Trendy", "C. Father Chewy Louie", "D. Father Dick Byrne"],
          ["A. Father Steel", "B. Father Stone", "C. Father Rock", "D. Father Wood"],
          ["A. Father Fredericks", "B. Father Duggan", "C. Father Finnegan", "D. Father Leopold"],
          ["A. Inis Mor (Aran Islands)", "B. Achill Island", "C. Clare Island", "D. Skellig Michael?"]]

questions = {
 "What is the longest river in the world?: ": "B",
 "What is the capital city of Malta?: ": "C",
 "In which country would you find a city called Sighisoara?: ": "A", 
 "In which city would you find the 'Spanish Steps'?: ": "B",
 "What is the largest lake in the world?: ": "C"
}

answers = [["A. River Liffey", "B. Amazon River", "C. Corrib River", "D. River Shannon "],
          ["A. Dublin", "B. Cork", "C. Valletta", "D. Belfast"],
          ["A. Romania", "B. England", "C. Poland", "D. Scotland"],
          ["A. Barcelona, ", "B. Rome ", "C. Dublin ", "D. London "],
          ["A. Lough Owel", "B. Lough Swilly", "C. Caspian Sea ", "D. Lough Derravaragh?"]]

def main():
   menu()


"""
    Do I need clear terminal. if so decide where best
    .
"""
def clear_terminal():
    os.system('clear')

"""
    Display menu option to users
"""
def menu():
    print("************Welcome to Quizeroo**************")
    print()

    choice = input("""
           1: Play Game
           2: Read Rules
           3: Quit

           Please enter your choice: 
           """)

    if choice == "1":
        play_game()
    elif choice == "2":
        read_rules()
    elif choice == "3":
        # exits the program
        sys.exit("Goodbye, please call again soon!")      
    else:
        print("!!!Please select either 1.(Play Game) or 2. (Read Rules)!!!")
        print()
        menu()

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

    quiz_topic = input("What quiz topic would you like to choose (A. Fr. Ted, B. 80s Pop Music, or C. Geography): ")
    
    for question in questions:
        print("-------------------------")
        print(question)
        for i in answers[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(question), guess)
        question_num += 1

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
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Actual Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
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
    else:
        return False

"""
    Run program functions
"""
main()

while replay_game():
    play_game()

print("Goodbye, please call again soon!")

