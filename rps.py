# ROCK, PAPER, SCISSORS

import random


def random_choice():
    choice = random.choice(["rock", "paper", "scissors"])
    return choice
    

def winner(player1, player2):
    if player1 == player2:
        return "Its a tie!"
    elif player1 == "rock" and player2 == "paper":
        return "Player 2 wins!"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 wins!"
    elif player1 == "paper" and player2 == "scissors":
        return "Player 2 wins!"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 wins!"
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 wins!"
    elif player1 == "scissors" and player2 == "rock":
        return "Player 2 wins!"

while True: # added BONUS to allow multiple games - whilst true, continue looping through game
    player1 = random_choice()
    player2 = random_choice()

    print(f"PLayer 1 chose: {player1}")
    print(f"PLayer 2 chose: {player2}")

    result = winner(player1, player2)

    print(result)

    # Ask the player if they want to play another round
    play_again = input("Do you want to play again? (yes/no): ").lower()

    # Exit the loop if the player says no
    if play_again != "yes":
        print("Thanks for playing!")
        break

    player1 = input("Enter your choice (rock, paper, or scissors): ").lower()

    # # adding this into the while True loop would allow for player 1 (me) to input the answer in the terminal

    # if player1 not in ["rock", "paper", "scissors"]:
    #     print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
    #     continue  # Restart the loop if the input is invalid