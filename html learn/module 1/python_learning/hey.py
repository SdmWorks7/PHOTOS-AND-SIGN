class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance +=amount
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds")
    def show_balance(self):
        print(f"The remaining balance is: {self.balance}")

account = BankAccount("Saumyadeep", 1000)
account.show_balance()
account.deposit(500)
account.show_balance()
account.withdraw(200)
account.show_balance()
account.withdraw(2000)
