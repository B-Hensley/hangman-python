import random
import string
# Make sure you have an 'animals_list.py' file with a list named 'animals'.
from animals_list import animals 
from hangman import hangman_stages

# Builds the hangman character from head to legs.
hangman_stages.reverse()
CHOICES = ['y', 'n']
LETTERS = list(string.ascii_lowercase)

replay = False

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
    
def start_game():
    start = ''
    
    # Checks if the start input is a yes or no and repeats question if not.
    while start not in CHOICES:
        start = input("Do you want to play Hangman? The category is animals. (y/n): ").lower()
        
        if start == 'y':
            return True
        elif start == 'n':
            return False
        else:
            print("Please enter a y or n.\n")
            
def play_again():
    again = ''
    
    # Checks if the again input is a yes or no and repeats question if not.
    while again not in CHOICES:
        again = input('Would you like to play again? (y/n): ')
        
        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Please enter a y or n.\n")
            
            
def run_game():
    global replay
    
    # Create new word each time run_game is called.
    word = random.choice(animals).lower()
    attempts = 6
    
    # Stores the correct and incorrect guesses
    correct_letters = []
    incorrect_letters = []
    
    if replay == False:
        start = start_game()
    else:
        start = True
    
    while start:
        replay = False
        
        print(f"Attempts Left: {attempts}")
        print(hangman_stages[attempts])
        
        display_word = ''
        
        # Replaces "_" with correct characters as they are guessed.
        for char in word:
            if char in correct_letters:
                display_word += char
            else:
                display_word += '_'
                
        print(display_word)
        
        # Logic to check if the player lost:
        if attempts == 0:
            print(f"\nYou Lose! The word was: {word}")
            replay = play_again()
            if replay:
                run_game()
            else:
                print('Thanks for playing my game! Check out my GitHub for more projects!')
                quit()
        
        if '_' not in display_word:
            print("You Won!")
            replay = play_again()
            if replay:
                run_game()
            else:
                print('Thanks for playing my game! Check out my GitHub for more projects!')
                quit()
        
        guess = player_guess(correct_letters, incorrect_letters)
        if guess in word:
            correct_letters.append(guess)
        else:
            incorrect_letters.append(guess)
            attempts -= 1
    

run_game()