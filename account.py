class Account:
    def __init__(self,name,balance):
        #handling account creation
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("insufficient balance")
            return False
        
    def get_balance(self):
        return self.balance