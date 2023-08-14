#import turtle
#timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("limegreen")
# timmy.forward(100)
# my_screen = Screen() # my_screen in object, Screen is class
# print(my_screen.canvheight) # canvheight is attribute
# # car.stop() # stop is method
# my_screen.exitonclick()

# from prettytable import PrettyTable

### Settings -> Project -> interpretter -> add package -> search prettytable -> add ###

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from day16-data import Menu, MenuItem
from day16-data import CoffeeMaker
from day16-data import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

