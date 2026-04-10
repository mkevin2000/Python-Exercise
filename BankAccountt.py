class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, balance):
        self.balance += balance
    def withdraw(self, balance):
        self.balance -= balance
    def __str__(self):
        return f"{self.name} has {self.balance} Dollars."    
c1 = BankAccount(" Quenan", 100)
assert c1.name == " Quenan"
assert c1.balance == 100
c1.deposit(50)
assert c1.balance == 150
c1.withdraw(30)
assert c1.balance == 120
print(c1)

