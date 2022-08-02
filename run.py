# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Player:
    """
    Define player class
    """
    def __init__(self, first_name, last_name, age, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown

    def __str__(self):
        return f"Greetings {self.first_name} {self.last_name} from {self.hometown}, Hello and Welcome to Quizeroo!!"


def main():

    fname = input("Please enter your first name \n")
    lname = input("Please enter your last name \n")
    age = int(input("Please enter your age \n"))
    hometown = input("What is your home town \n")

    new_player = Player(fname, lname, age, hometown)
    print (f"{new_player}")

    ans = input("Are you ready to play (Yes/No:) ")
    print(ans)
    score = 0
    total_questions = 10

    if ans.lower() == 'yes':
        ans = input ("1. What is the highest mountain in the world? ")
        if ans.lower() == 'everest' or ans.lower() == 'mount everest':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Mount Everest is the worlds highest mountain.")

        ans = input ("2. What is the longest river in the world? ")
        if ans.lower() == 'amazon' or ans.lower() == 'amazon river':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Amazon River is the worlds longest river.")

        ans = input ("3. What is the capital city of Malta? ")
        if ans.lower() == 'valletta':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Valletta is the capital city of Malta.")

        ans = input ("4. In which country would you find a city called Sighisoara? ")
        if ans.lower() == 'romania':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Sighisoara is a city in Romania.")

        ans = input ("5. In which city would you find the 'Spanish Steps'? ")
        if ans.lower() == 'rome':
            score += 1
            print("Correct")
        else:
            print("Incorrect. The 'Spanish Steps' are in Rome, Italy")

        ans = input ("6. What is the largest lake in the world'? ")
        if ans.lower() == 'caspian' or ans.lower()=='caspian sea':
            score += 1
            print("Correct")
        else:
            print("Incorrect. The largest lake in the world is the Caspian Sea")

        ans = input ("7. In which country would you find the capital city of Ljubljana? ")
        if ans.lower() == 'slovenia':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Ljubljana is the capital city of Slovenia?")

        ans = input ("8. What is the largest country in the world? ")
        if ans.lower() == 'russia':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Russia is the largest country in the world")

        ans = input ("9. What is the smallest country in the world? ")
        if ans.lower() == 'vatican' or ans.lower() == 'vatican city':
            score += 1
            print("Correct")
        else:
            print("Incorrect. Vatican City  is the smallest country in the world")

        ans = input ("10. Which country in the world has most borders? ")
        if ans.lower() == 'china':
            score += 1
            print("Correct")
        else:
            print("Incorrect. China has the most borders with 14 neighbouring countries")

        print(score)
        print(f"Thank you for playing {fname}")
        print(f"You got {score} questions correct out of {total_questions}")
        mark = (score/total_questions)*100
        print("That's a score of", str(mark) + '%')

    print("Goodbye. Maybe call back another time to play Quizeroo!")

main()
