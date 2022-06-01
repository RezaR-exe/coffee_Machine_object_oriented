# # welcome to my coffee shop! This program is console only! So no graphics, it's a training program that I started #
# creating by learning python and object-oriented programming
# the concept is clear, you are a customer, and you want a type of coffee, you will need to tell the program
# exactly what type of coffee you want and insert
# the needed money, and the machine will automatically
# calculate if there is enough money or resources in the
# machine to prepare your drink!
# you can contact me at panait446@gmail.com
# or on my LinkedIn https://www.linkedin.com/in/andrei-daniel-panait-225678226/
# # have fun and thank you so much for trying my app, happy coding :)!

from res import resources
from order import CoffeeMaker
from order import CheckResources

machine_is_running = True

while machine_is_running:
    CheckResources()
    print("Hello! Please specify which drink you want!")
    print("Here's our coffee menu: ")
    print("Latte\nCappuccino\nEspresso\nMachiato\nHot Chocolate\nMoccha\nPlease specify each drink with"
          " capital letter: ")
    response = input()

    if response == "fill":
        resources['milk'] = 1000
        resources['water'] = 1000
        resources['coffee'] = 1000
        resources['sugar'] = 1000
        resources['cocoa'] = 1000

    elif response == "res":
        print(resources["milk"])
        print(resources["coffee"])
        print(resources["water"])
        print(resources['sugar'])
        print(resources['cocoa'])
        machine_is_running = False
    elif response == "Latte":
        latte = CoffeeMaker(response)
        latte.drink = "latte"
        sugar = input("Do you wish sugar? (extra $0.75)")
        if sugar == "yes":
            if latte.WantSugar():
                print("Got it! We will add sugar to your drink!")
                latte.cost = 3.25
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                latte.cost = 2.50
        elif sugar == "no":
            print("got it!")
            latte.cost = 2.50
        insert_money = float(input(f"Please insert the money into the machine ({latte.cost}): "))
        if latte.CheckResources():
            if latte.CalculateMoney(insert_money):
                if latte.cost < insert_money:
                    rest = insert_money - latte.cost
                    print(f"Your rest of {rest}$ will be deducted on your right.")
                    print(f"Enjoy your {latte.drink}! Have a great day!")
                else:
                    print(f"Enjoy your {latte.drink}! Have a great day!")
            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            print(f"You can claim your {insert_money}$ on your right.")
            machine_is_running = False

    elif response == "Cappuccino":
        cappuccino = CoffeeMaker(response)
        cappuccino.drink = "cappuccino"
        sugar = input("Do you wish sugar? (extra $0.75)")
        if sugar == "yes":
            if cappuccino.WantSugar():
                print("Got it! We will add sugar to your drink!")
                cappuccino.cost = 4.25
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                cappuccino.cost = 3.50
        elif sugar == "no":
            print("got it!")
            cappuccino.cost = 3.50
        insert_money = float(input(f"Please insert money ({cappuccino.cost}): "))
        if cappuccino.CheckResources():
            if cappuccino.CalculateMoney(insert_money):
                if cappuccino.cost < insert_money:
                    rest = insert_money - cappuccino.cost
                    print(f"Your rest of {rest}$ will be deducted on your right.")
                    print(f"Enjoy your {cappuccino.drink}! Have a great day!")
                else:
                    print(f"Enjoy your {cappuccino.drink}! Have a great day!")
            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            print(f"You can claim your {insert_money}$ on your right.")
            machine_is_running = False
    elif response == "Espresso":
        espresso = CoffeeMaker(response)
        espresso.drink = "espresso"
        sugar = input("Do you wish sugar? (extra $0.75)")
        if sugar == "yes":
            if espresso.WantSugar():
                print("Got it! We will add sugar to your drink!")
                espresso.cost = 6.25
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                espresso.cost = 5.50
        elif sugar == "no":
            print("got it!")
            espresso.cost = 5.50
        insert_money = float(input(f"Please insert money ({espresso.cost}): "))
        if espresso.CheckResources():
            if espresso.CalculateMoney(insert_money):
                if espresso.cost < insert_money:
                    rest = insert_money - espresso.cost
                    print(f"Your rest of {rest}$ will be deducted on your right.")
                    print(f"Enjoy your {espresso.drink}! Have a great day!")
                else:
                    print(f"Enjoy your {espresso.drink}! Have a great day!")
            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            machine_is_running = False
    elif response == "Machiato":
        machiato = CoffeeMaker(response)
        machiato.drink = "machiato"
        sugar = input("Do you wish sugar? (extra $0.75)")
        if sugar == "yes":
            if machiato.WantSugar():
                print("Got it! We will add sugar to your drink!")
                machiato.cost = 4.50
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                machiato.cost = 3.75
        elif sugar == "no":
            print("got it!")
            machiato.cost = 3.75
        insert_money = float(input(f"Please insert money ({machiato.cost}): "))
        if machiato.CheckResources():
            if machiato.CalculateMoney(insert_money):
                if machiato.cost < insert_money:
                    rest = insert_money - machiato.cost
                    print(f"Your rest of {rest}$ will be deducted on your right.")
                    print(f"Enjoy your {machiato.drink}! Have a great day!")
                else:
                    print(f"Enjoy your {machiato.drink}! Have a great day!")
            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            print(f"You can claim your {insert_money}$ on your right.")
            machine_is_running = False
    elif response == "Hot Chocolate":
        hotchocolate = CoffeeMaker(response)
        hotchocolate.drink = "hotchocolate"
        sugar = input("Do you wish extra sugar? (extra $0.75)")
        if sugar == "yes":
            if hotchocolate.WantSugar():
                print("Got it! We will add sugar to your drink!")
                hotchocolate.cost = 5.50
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                hotchocolate.cost = 4.75
        elif sugar == "no":
            print("got it!")
            hotchocolate.cost = 4.75
        insert_money = float(input(f"Please insert money ({hotchocolate.cost}): "))
        if hotchocolate.CheckResources():
            if hotchocolate.CalculateMoney(insert_money):
                if hotchocolate.cost < insert_money:
                    rest = insert_money - hotchocolate.cost
                    print(f"Your rest of {rest}$ will be deducted on your right.")
                    print(f"Enjoy your {hotchocolate.drink}! Have a great day!")
                else:
                    print(f"Enjoy your {hotchocolate.drink}! Have a great day!")
            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            print(f"You can claim your {insert_money}$ on your right.")
            machine_is_running = False
    elif response == "Moccha":
        moccha = CoffeeMaker(response)
        moccha.drink = "moccha"
        sugar = input("Do you wish extra sugar? (extra $0.75)")
        if sugar == "yes":
            if moccha.WantSugar():
                print("Got it! We will add sugar to your drink!")
                moccha.cost = 6.50
            else:
                print("We're sorry, we ran out of sugar. we will refill it ASAP")
                moccha.cost = 5.75
        elif sugar == "no":
            print("Got it!")
            moccha.cost = 5.75
        insert_money = float(input(f"Please insert money ({moccha.cost}): "))
        if moccha.CheckResources():
            if moccha.CalculateMoney(insert_money):
                if moccha.cost < insert_money:
                    rest = insert_money - moccha.cost
                    print(f"Enjoy your {moccha.drink}!")
                    print(f"The rest of {rest}$ will be deducted on your right. Have a nice day!")
                else:
                    print(f"Enjoy your {moccha.drink}!")

            else:
                print("There is not enough money in the machine for the specified drink. Please try again.")
                print(f"You can claim your {insert_money}$ on your right.")
        else:
            print("There are not enough resources available for that drink. Please come back later!")
            print(f"You can claim your {insert_money}$ on your right.")
            machine_is_running = False
    else:
        print("This drink is not on our menu. Please specify a drink available on our menu.")
