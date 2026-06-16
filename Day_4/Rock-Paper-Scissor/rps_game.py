import random as r
import rock_paper_scissor_text as rps

player_choice = int(input("What do you choose?\n" \
"Type 0 for Rock\n" \
"Type 1 for Paper\n" \
"Type 2 for Scissor\n"))

computer_choice = r.randint(0,2)

print("Your choice: ")
print(rps.rps[player_choice])

print()

print("Computer chose: ")
print(rps.rps[computer_choice])

if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == 0 and computer_choice == 1:
    print("You loose.")
elif player_choice == 1 and computer_choice == 2:
    print("You loose.")
elif player_choice == 2 and computer_choice == 0:
    print("You loose.")
else:
    print("You Win!!!")