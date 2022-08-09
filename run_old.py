#Netflix type system demo - FakeFlix
import csv
import sys

def main():
   menu()


def menu():
    print("************Welcome to FakeFlix Demo**************")
    print()

    choice = input("""
                      1: Play Game
                      2: Read Rules
                      3: Quit

                      Please enter your choice: """)

    if choice == "1":
        play_game()
    elif choice == "2":
        read_rules()
    elif choice == "3":
        sys.exit
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        menu()

def play_game():
   print("Play Game")
    
def read_rules():
   print("Read Rules")
    
#the program is initiated, so to speak, here
main()

