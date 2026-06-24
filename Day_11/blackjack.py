from art import logo
from random import randint
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        return True
    else:
        return False


def get_card():
    return cards[randint(0, 12)]


def has_blackjack(mylist):
    if [10, 11] in mylist and mylist.len() == 2:
        return True
    else:
        return False


def has_ace():
    global player_hand
    if 11 in player_hand:
        player_hand[player_hand.index(11)] = 1
        has_ace()
    else:
        return player_hand


def get_score(mylist):
    if has_blackjack(mylist):
        return 21
    else:
        total = 0
        for num in mylist:
            total += num
        if total > 21:
            mylist = has_ace()
            get_score(mylist)

    return total


# deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while play_game():
    # print logo of game
    clear()
    print(logo)

    # list containing cards in hand for player and computer
    player_hand = []
    computer_hand = []

    # variable to hold scores
    player_score = 0
    computer_score = 0

    # get first round of cards
    player_hand.append(get_card())
    computer_hand.append(get_card())

    # get second round of cards
    player_hand.append(get_card())
    computer_hand.append(get_card())

    player_score = get_score(player_hand)
    computer_score = get_score(computer_hand)

    print(player_hand, player_score)
    print(computer_hand, computer_score)
