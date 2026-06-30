from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    user_order = input(f"What would you like {menu.get_items()}? ").lower()

    if user_order == 'off':
        break

    elif user_order == "print":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(user_order) and coffee_maker.is_resource_sufficient(menu.find_drink(user_order)):
        while not money_machine.make_payment(menu.find_drink(user_order).cost):
            pass
        coffee_maker.make_coffee(menu.find_drink(user_order))
        