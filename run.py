import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def clear_terminal():
    os.system('clear')

def display_menu():
    print("Option 1 - Play game")
    print("Option 2 - Read rules")
    print("Option 3 - Quit game")

    user_choice = input("What would you like to do here? Please enter 1, 2 or 3 ")

    if user_choice == 2: 
        setup_game()

def setup_game():
    print("Welcome to Quizeroo!!")

    print(
        f"""{Fore.GREEN+Style.BRIGHT}
            
        ░██████╗░██╗░░░██╗██╗███████╗███████╗██████╗░░█████╗░░█████╗░
        ██╔═══██╗██║░░░██║██║╚════██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
        ██║██╗██║██║░░░██║██║░░███╔═╝█████╗░░██████╔╝██║░░██║██║░░██║
        ╚██████╔╝██║░░░██║██║██╔══╝░░██╔══╝░░██╔══██╗██║░░██║██║░░██║
        ░╚═██╔═╝░╚██████╔╝██║███████╗███████╗██║░░██║╚█████╔╝╚█████╔╝
        ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░░╚════╝░
        """
        )

print("Hello Elaine")
display_menu()
# setup_game()
# clear_terminal()

# setup_game()
# main()
# display_results() 

