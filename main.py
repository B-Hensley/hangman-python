import random
import string
# Make sure you have an 'animals_list.py' file with a list named 'animals'.
from animals_list import animals 
from hangman import hangman_stages

# Builds the hangman character from head to legs.
hangman_stages.reverse()
CHOICES = ['y', 'n']
LETTERS = list(string.ascii_lowercase)

# Select a random word from the list and initialize variables.
word = random.choice(animals).lower()

# Starts the game by asking player to choose if they would like to play or not. If yes, prompt player to guess letter.
def start():
    start_game = False
    choice = ''
    while choice.lower() not in CHOICES:
        choice = input("Do you want to play Hangman? The subject is animals. (y/n):  ")
        if choice.lower() == 'y':
            start_game = True
            return start_game
        
        elif choice.lower() == 'n':
            start_game = False
            print("Maybe later!")
            return start_game
        
        else:
            start_game = False
            print("Please enter y or n!")
            return start_game

# This function gathers the users letter guess/choice for the game and validates that it's a letter.
def player_guess(correct_guesses, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        
        # Tells player if they have guessed a letter before.
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed this letter. Try again.")
            
        else:
            if guess in LETTERS and len(guess) == 1:
                return guess
            print("Please enter a single letter.")

# This function allows the player to play again, or to choose not to play again and ends the program.
def run_again():
    choice = ''
    while choice.lower() not in CHOICES:
        choice = input("Do you want to play Hangman again? The subject is animals. (y/n):  ")
        if choice.lower() == 'y':
            return True
        
        elif choice.lower() == 'n':
            print("Maybe later!")
            return False
        
        else:
            print("Please enter y or n!")


# Runs the game
def run_game(start_game):
    
    # Select a random word from the list and initialize variables.
    word = random.choice(animals).lower()

    correct_letters = []
    incorrect_letters = []
    attempts = 6

    while start_game:
        
        print(f'Attempts left: {attempts}')
        
        print(hangman_stages[attempts])
        
        display_word = ''
        
        # Replaces "_" with correct characters as they are guessed.
        for char in word:
            if char in correct_letters:
                display_word += char
            else:
                display_word += '_'
                
        print(display_word)
        
        # Checks to see if there are any remaining spaces to guess for.
        if '_' not in display_word:
            print("You Win!")
            restart_game = run_again()
            if restart_game:
                run_game(start_game)
            else:
                print("Thanks for playing!")
                break
        
        # Checks attempts to determine if attempts have all been used, if attempts is 0 and there are still "_", then player loses.
        if attempts == 0:
            print(f"You lose! The word was {word}.")    
            restart_game = run_again()
            if restart_game:
                run_game(start_game)
            else:
                print("Thanks for playing!")
                break        
        # Keeps a list of correct and incorrect letters guessed by player; used to tell player if they have already guessed a letter.
        guess = player_guess(correct_letters, incorrect_letters)
        if guess in word:
            correct_letters.append(guess)
        else:
            incorrect_letters.append(guess)
            attempts -= 1
            

start_game = start()
run_game(start_game)