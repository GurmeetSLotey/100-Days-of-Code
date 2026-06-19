import random as r
import string
import art

print(art.logo)

all_letters = list(string.ascii_letters)
play = True

while play:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    message = list(input("Type your message:\n"))
    shift = int(input("Type the shift number:\n")) % len(all_letters)

    if choice == 'decode':
        shift *= -1

    for index, letter in enumerate(message):
        message[index] = all_letters[all_letters.index(letter) + shift]

    print(f"Here's the {choice}d result: {"".join(message)}")

    user_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

    if user_again != 'yes':
        play = False

print("goodbye")