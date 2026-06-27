"""
User is given two options to choose from in this case it'll be
two people. The user will select option A or B for whom they believe
has a higher count of followers on social media. 
If the user guesses correctly their score will increase by one.
If the user guesses incorrectly it'll be game over and their score will be displayed
"""

import art
import game_data as gd
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_choice():
    return random.choice(list(gd.data))

def compare(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'
    

print(art.logo)

score = 0

while True:
    compare_a = random_choice()
    compare_b = random_choice()
    while compare_b['follower_count'] == compare_a['follower_count']:
        compare_b = random_choice()
    
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}.")
    print(art.vs)
    print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    clear()
    if choice == compare(a = compare_a, b = compare_b):
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}.")
    else:
        break

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")