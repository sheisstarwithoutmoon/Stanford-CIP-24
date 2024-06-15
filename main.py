"""
File: main.py
-------------------
This program is a game where you have to guess a 5 letter word by giving 5 letter word 
as a guess that you think might be in the secret word. You are given 6 attempts.
If you get to 0 points, the game ends and you lose.
If you guessed correctly, the letter you guessed will be displayed in green if it is the same position of it
otherwise in yellow.
If your guess is not a valid word, no lives will be taken and your progress will remain the same.

Thank you to the entire Code in Place team for providing the knowledge I used in creating this program. 
Your engaging classes and references to real world made the learning experience enjoyable. 
I thoroughly enjoyed Code in Place and have decided to continue my programming journey.
 
"""
import random

guesses_dict = "valid_words.txt"     #File of valid words
answers_dict = "words.txt"           #File to take secret words from
max_attempts = 6                     #Maximum number of attempts

def instructions():
    '''
    This function lists out all the necessary instructions.
    '''
    print("INSTRUCTIONS:")
    print("1. The word consists of 5 letters.")
    print("2. Press 'enter' to see if any letters in it are also in the word.")
    print("3. You have 6 attempts to guess the word.")
    print("4. If the letter is in the correct place, it will be shown in green; otherwise, in yellow.\n")

def load_words(file_path):
    '''
    This function loads the words from the file.
    '''
    with open(file_path, 'r') as f:
        words = [line.strip().lower() for line in f]
    return words

def choose_word(words):
    '''
    This function returns a secret word that the player will try
    to guess in the game. It takes words from the file "guesses_dict"
    defined as a constant at the beginning of the program.
    '''
    return random.choice(words).strip().upper()

def is_valid_guess(guess, guesses):
    '''
    This function checks that the guess is valid or not by checking it's length and checking 
    if the word is present in file valid_words.txt
    '''
    return len(guess) == 5 and guess in guesses

def evaluate_guess(guess, word):
    '''
    This function checks whether the guessed word letters are present in the secret_word or not
    If guessed word letters are present in the secret_word, the letter you guessed will be displayed 
    in green if it is the same position of it otherwise in yellow.
    '''
    message = ""

    for i in range(5):
        if guess[i] == word[i]:
            message += "\033[32m" + guess[i]  # Green for correct letter in the correct position
        elif guess[i] in word:
            message += "\033[33m" + guess[i]  # Yellow for correct letter in the wrong position
        else:
            message += "\033[0m" + guess[i]   # Default color for incorrect letter
    
    return message + "\033[0m"

def wordle(guesses, answers):
    '''
    This function handles the main game loop for Wordle.
    It tracks the number of attempts and provides feedback on each guess.
    '''
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")
    secret_word = choose_word(answers).lower()

    attempts = 0

    while attempts < max_attempts:
        guess = input("Enter Guess " + str(attempts + 1) + ": ").lower()
        
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue

        attempts += 1

        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
    
    if attempts == max_attempts and guess != secret_word:
        print("Game over. The secret word was:", secret_word)
        print("-Created by Vanya")

def main():
    guesses = load_words(guesses_dict)
    secret_word = load_words(answers_dict)
    
    instructions()
    wordle(guesses, secret_word)

if __name__ == "__main__":
    main()
