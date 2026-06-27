from packages.ingredients import MENU
from packages.ingredients import resources
from packages.ingredients import coins
import packages.art as art
import subprocess
import platform

def clear():
    command = "cls" if platform.system() == "Windows" else "clear"

    subprocess.run(command, shell=True)

def check_resources(order):
    cost = MENU[order]['cost']
    for k, v in MENU[order]['ingredients'].items():
        if resources[k] < v:
            print(f"Sorry we don't have enough {k} to make your order.")
            return False
    return True

def make_order(order):
    for k, v in MENU[order]['ingredients'].items():
        resources[k] -= v

def get_cost(order):
    return MENU[order]['cost']

def get_coins(cost):
    total_paid = 0

    while total_paid < cost:

        print("Please insert coins.")
        # quarters = int(input("How many quarters?: "))
        # dimes = int(input("How many dimes?: "))
        # nickles = int(input("How many nickles?: "))
        # pennies = int(input("How many pennies?: "))

        for k, v in coins.items():
            total_paid += int(input(f"How many {k}?: ")) * v

        print(f"You have paid {total_paid}")

    resources['money'] += cost

    if total_paid > cost:
        print(f"Your change is {total_paid - cost}")

def print_inventory():
    for k,v in resources.items():
        print(f"Current inventory of {k} is: {v}.")


clear()

print(art.logo)

while True:

    # get users input on kind of coffee they'd like
    user_choice = input("What would you like? (espresso / latte / cappuccion): ").lower()

    # coffee machine turns off when user inputs off
    if user_choice == 'off':
        print("Shutting off")
        break

    # print report
    #   water, milk, coffee and money in stock
    elif user_choice == 'print':
        print_inventory()

    #   check for sufficient resources
    elif check_resources(user_choice):
        make_order(user_choice)
        cost = get_cost(user_choice)
        print(f"You are ordering a {user_choice}, the cost of your order is: {cost}. ")

        #   process coins, ask for more if needed or give change back if needed
        #   check transaction succesfull
        get_coins(cost)

        print(f"Thank you! Here is your order of {user_choice} ☕️")