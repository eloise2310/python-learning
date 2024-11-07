# MAKING AN INTERACTIVE DICE ROLLING GAME (rolling two dice)

import random # allows access to randint (random integer)

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6) # twice because its rolling two dice 
    return dice_total

# lets players input their own name - \n lets them input it on the next line 
player1 = input("Enter player 1's name:\n")
player2 = input("Enter player 2's name:\n")

roll1 = roll_dice() # player 1's roll
roll2 = roll_dice() # player 2's roll

# prints total of each roll 
print(f"{player1} rolled {roll1}") 
print(f"{player2} rolled {roll2}")

# prints who the winner is 
if (roll1 > roll2):
    print(f"{player1} wins!")
elif (roll2 > roll2):
    print(f"{player2} wins!")
else:
    print("Its a tie!")