class CoffeeMachine:
    coffee_machine_existence = 0
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550

    def __new__(cls):
        if cls.coffee_machine_existence < 1:
            cls.coffee_machine_existence += 1
            return object.__new__(cls)

    def __init__(self):
        self.start()

    def start(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input("> ")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
                print()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.machine_status()
                print()
                continue
            elif action == "exit":
                break

    def machine_impact(self, water_x, milk_x, coffe_beans_x, disposable_cups_x, money_x):
        self.water += water_x
        self.milk += milk_x
        self.coffee_beans += coffe_beans_x
        self.disposable_cups += disposable_cups_x
        self.money += money_x

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - back to main menu:")
        coffee_type = input("> ")

        def coffee_check(water_check, milk_check, coffee_beans_check, disposable_cups_check):
            if self.water >= water_check and self.milk >= milk_check and self.coffee_beans >= coffee_beans_check \
                    and self.disposable_cups >= disposable_cups_check:
                return True
            elif self.water < water_check:
                print("Sorry, not enough water")
                return False
            elif self.milk < milk_check:
                print("Sorry, not enough milk")
                return False
            elif self.coffee_beans < coffee_beans_check:
                print("Sorry, not enough coffe beans")
                return False
            elif self.disposable_cups < disposable_cups_check:
                print("Sorry, not enough disposable cups")
                return False

        if coffee_type == "back":
            print()
        elif int(coffee_type) == 1:
            coffee_possibility = coffee_check(250, 0, 16, 1)
            if coffee_possibility:
                self.machine_impact(-250, -0, -16, -1, 4)
                print("I have enough resources, making you a coffee!", end="\n\n")
        elif int(coffee_type) == 2:
            coffee_possibility = coffee_check(350, 75, 20, 1)
            if coffee_possibility:
                self.machine_impact(-350, -75, -20, -1, 7)
                print("I have enough resources, making you a coffee!", end="\n\n")
        elif int(coffee_type) == 3:
            coffee_possibility = coffee_check(200, 100, 12, 1)
            if coffee_possibility:
                self.machine_impact(-200, -100, -12, -1, 6)
                print("I have enough resources, making you a coffee!", end="\n\n")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        water_add = int(input("> "))
        print("Write how many ml of milk do you want to add:")
        milk_add = int(input("> "))
        print("Write how many grams of coffee beans do you want to add:")
        coffee_beans_add = int(input("> "))
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups_add = int(input("> "))
        self.machine_impact(water_add, milk_add, coffee_beans_add, disposable_cups_add, 0)

    def machine_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


# ======================
use_coffee_machine = CoffeeMachine()
