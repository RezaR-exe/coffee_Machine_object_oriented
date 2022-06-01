from res import resources


class CoffeeMaker():
    def __init__(self, drink):
        self.drink = drink
        self.milk = 0
        self.coffee = 0
        self.water = 0
        self.cost = 0
        self.sugar = 0

    def CheckResources(self):
        if self.drink == "latte":
            self.milk = 50
            self.water = 50
            self.coffee = 50
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                resources['milk'] -= self.milk
                resources['water'] -= self.water
                resources['coffee'] -= self.coffee
                return True
        elif self.drink == "cappuccino":
            self.milk = 10
            self.water = 10
            self.coffee = 100
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                resources['milk'] -= self.milk
                resources['water'] -= self.water
                resources['coffee'] -= self.coffee
                return True
        elif self.drink == "espresso":
            self.milk = 0
            self.water = 30
            self.coffee = 200
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                resources['milk'] -= self.milk
                resources['water'] -= self.water
                resources['coffee'] -= self.coffee
                return True
        elif self.drink == "machiato":
            self.milk = 0
            self.water = 30
            self.coffee = 200
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                return True
        elif self.drink == "hotchocolate":
            self.milk = 0
            self.water = 30
            self.coffee = 200
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                resources['milk'] -= self.milk
                resources['water'] -= self.water
                resources['coffee'] -= self.coffee
                return True
        elif self.drink == "moccha":
            self.milk = 0
            self.water = 30
            self.coffee = 200
            if resources['milk'] < self.milk or resources['coffee'] < self.coffee or resources['water'] < self.water:
                return False
            else:
                resources['milk'] -= self.milk
                resources['water'] -= self.water
                resources['coffee'] -= self.coffee
                return True

    def CalculateMoney(self, money):
        if self.drink == "latte":
            if money < self.cost:
                return False
            else:
                return True
        elif self.drink == "cappuccino":
            if money < self.cost:
                return False
            else:
                return True
        elif self.drink == "espresso":
            if money < self.cost:
                return False
            else:
                return True
        elif self.drink == "machiato":
            if money < self.cost:
                return False
            else:
                return True
        elif self.drink == "hotchocolate":
            if money < self.cost:
                return False
            else:
                return True
        elif self.drink == "moccha":
            if money < self.cost:
                return False
            else:
                return True

    def WantSugar(self):
        self.sugar = 20
        if resources['sugar'] < self.sugar:
            return False
        else:
            resources['sugar'] -= self.sugar
            return True



def CheckResources():
    if resources['milk'] < 200 or resources['water'] < 200 or resources['coffee'] < 200 or resources['sugar'] < 200 or resources['cocoa'] < 200:
        print("Running low on resources, please call an administrator ASAP.")