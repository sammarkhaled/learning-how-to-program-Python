#game of guessing the number
import random

def game():
    
    print("Welcome to the GAME OF GUESSING, where you have a number of tries to guess a number between 0 - 100!")

    number = random.randint(int(input("choose a minimum : ")), int(input("choose a maximum : ")))
    usedTries = 0
    tries = int(input("Choose the number of trials : "))

    while tries > 0:
        guess = int(input("Type in your guess player : "))
        usedTries += 1

        if guess < 0 or guess > 99:
            print("Your chosen number is not in the range of possible numbers (0 - 99)")

        elif number < guess:
            print("Your number is too big, choose a smaller one ;)")

        elif number > guess:
            print("Your number is too small, choose a bigger one ;)")

        else:
            if usedTries > 1:
                print(f"The number {number} is correct, congrats you won the game and needed {usedTries} tries!!!")
                return
            
            else:
                print(f"The number {number} is correct, congrats you won the game and only needed {usedTries} try!!!")
                return
            
        tries -= 1

    print(f"GAME OVER, the correct number was {number}")
game()