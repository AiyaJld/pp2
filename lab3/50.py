class Account():
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    
    def __str__(self):
        return f'Acc owner: {self.owner}, acc balance: {self.balance}'
    def deposit(self, dep_money):
        self.balance+=dep_money

    def withdraw(self, take_money):
        if take_money <= self.balance:
            self.balance-=take_money
            return  f'available, balance= {self.balance}' 
        else:
            return f'not available'
    

a=Account(str(input()), int(input()))
print(a)
a.deposit(int(input()))
print(a.balance)
print(a.withdraw(int(input())))
