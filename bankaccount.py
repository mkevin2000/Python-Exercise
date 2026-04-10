class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt
    def __str__(self):
        return f"Your account, {self.name}, has {self.amt} dollars."
t1= BankAccount("Bob", 100)    
print(t1)