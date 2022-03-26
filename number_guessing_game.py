import os
from random import randint
os.system('cls || clear')

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Set initial variable values
attempts_dict = {'easy':10,'hard':5}
attempts_left = attempts_dict[difficulty]
RANDOM_NUMBER = randint(1,100)
game_over = False

def check_guess(guess_nr):
    # Guessed correctly, you won!
    if guess_nr == RANDOM_NUMBER: return "Win"
    # Too high
    if guess_nr > RANDOM_NUMBER: return "Too high"
    # Too low
    if guess_nr < RANDOM_NUMBER: return "Too low"

# Start loop
while game_over != True:

    print(f"You have {attempts_left} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    result = check_guess(guessed_number)

    if result == "Win":
        print(f"The number was indeed {RANDOM_NUMBER}, you win!")
        game_over = True
    else:
        print(result)
        attempts_left -= 1

    if attempts_left == 0:
        print(f"You ran out of attempts, the number was {RANDOM_NUMBER}, you lose!") 
        game_over = True