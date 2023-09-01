class bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance= balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("Invalid Amount")
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance - amount
        else:
            print("Balance is low")
    def showBalance(self):
        print("Balance:",self.balance)
class Savings(bank):
    def __init__(self, name, balance,interest = 0.04):
        super().__init__(name, balance)
        self.interest = interest
    def calInterest(self):
        print("Interest:",self.balance * self.interest)
class current(bank):
    def __init__(self, name, balance,interest = 0.02):
        super().__init__(name, balance)
        self.interest = interest
    def calInterest(self):
        print("Interest:",self.balance*self.interest)
a = Savings("Kathir",500)
a.showBalance()
a.deposit(1000)
a.withdraw(200)
a.calInterest()
a.showBalance()
b = current("Kathir",500)
b.showBalance()
b.deposit(1000)
b.withdraw(200)
b.calInterest()
b.showBalance()