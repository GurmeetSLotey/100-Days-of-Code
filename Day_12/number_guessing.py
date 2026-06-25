import guess_the_number_art as art
import random

print(art.logo)
print("I'm thinking of a number between 1 and 100.")

num_of_tries = 0
random_number = random.randint(1,100)

# Easy mode is 10 tries Hard mode is 5 tries
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    num_of_tries = 10
elif difficulty == 'hard':
    num_of_tries = 5
else:
    num_of_tries = 1

# Guess number between 1 and 100
while num_of_tries > 0:
    print(f"You have {num_of_tries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    num_of_tries -= 1

    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        break
    elif num_of_tries == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        break
    elif guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")

    print("Guess again.")