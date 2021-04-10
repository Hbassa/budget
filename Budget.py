class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def deposit(self):
        amount = int(input("how much do you want to deposit to your budget? \n"))
        balance = (self.food + amount) + (self.clothing + amount) + (self.entertainment + amount)

        print("you have deposited %s to each category in your budget and your balance is %s" % (amount, balance))

    def withdraw(self):
        amount = int(input("how much do you want to withdraw from your budget? \n"))
        balance = (self.food - amount) + (self.clothing - amount) + (self.entertainment - amount)

        print("you have withrawn %s from each category in your budget and your balance is %s" % (amount, balance))

    def get_balance(self):
        balance = self.food + self.clothing + self.entertainment

        print("your balance is %s" % balance)

    def transfer(self):
        pass



budget_1 = Budget(100, 200, 300)
budget_2 = Budget(200, 300, 400)

budget_1.deposit()
budget_1.withdraw()
budget_1.get_balance()
budget_1.transfer()
