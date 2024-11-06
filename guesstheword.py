# GUESS THE WORD
# Create a simple game in which the user tries to guess a randomly selected word from a list of words
# the programme should provide feedback to the user after each guess
# indicating whether the guess was correct or not and allowing the user to continue guessing 

import random

word_list = ["this", "is", "a", "list", "of", "random", "words", "to", "guess"]

selected_word = random.choice(word_list)

while True:
    guess = input("Enter your guess: ").lower()

    if guess == selected_word:
        print("Congratulations! You guessted the word correctly!")
        break # ends the game
    else: 
        print("Wrong guess. Try again")