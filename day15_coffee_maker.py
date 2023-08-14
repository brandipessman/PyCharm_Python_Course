from data import menu
from data import resources

cont = True


def calculate_change(drink):
    print(f"Please insert coins. It costs ${menu[drink]['cost']}.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    paid = quarters + dimes + nickels + pennies
    if paid < menu[drink]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change = paid - menu[drink]['cost']
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink}. Enjoy!")


while cont == True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif order == "off":
        cont = False
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        milk = menu[order]['ingredients']['milk']
        water = menu[order]['ingredients']['water']
        coffee = menu[order]['ingredients']['coffee']
        if milk > resources['milk']:
            print("Sorry there is not enough milk.")
        elif water > resources['water']:
            print("Sorry there is not enough water.")
        elif coffee > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            calculate_change(order)
            resources['milk'] -= milk
            resources['water'] -= water
            resources['coffee'] -= coffee
            resources['money'] += menu[order]['cost']
