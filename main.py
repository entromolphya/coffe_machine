from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

while True:
    print("\nWhat would you like ? ( "+menu.get_items()+" )")

    drink=input().lower()

    if drink=="off":
        break
    elif drink=="report":
        coffee.report()
        money.report()
    else:
        ans=menu.find_drink(drink)
        pay = True
        if ans!=None:
           if coffee.is_resource_sufficient(ans):
                pay=money.make_payment(ans.cost)
           if pay==True:
                coffee.make_coffee(ans)
        # coffee.report()
        # money.report()

    x=input("want to buy any other drink ? 'y' or 'n' ").lower()
    if(x=='n'):
        break
    else:
        # To clear the screen:
        clear_screen()