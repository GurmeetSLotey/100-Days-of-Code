import gavel_art
import re
import os

def get_bid():
    while True:
        user_input = input("Enter a price (e.g., 10.50): ")
    
        # Matches optional digits, a dot, and exactly two digits at the end
        if re.match(r"^\d+\.\d{2}$", user_input):
            value = float(user_input)
            break
        else:
            print("Invalid format! Please enter exactly two decimal places.")

    print(f"Accepted bid: {value}")
    return value

print(gavel_art.gavel)

# Dictionary which will contain users and their bids
auction_bids = {}
bidding = True
max_bid = 0
winner = ''

while bidding:

    # Get users name
    user = input("What is your name?: ")
    
    # Get bid
    bid = get_bid()

    # Add bid to dictionary and see if the bid is the new maximum
    auction_bids(user) = bid
    if bid > max_bid:
        max_bid = bid
        winner = user

    # Ask if there are any other bidders
    add_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    #   if so get their bid
    if add_more_bidders != 'yes':
        break

    #   else clear screen and get next bidder info
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


# Once all bids are gotten, display the winner's name and bid amt
print(f'The winning bid is from {winner} in the amount of {max_bid}')