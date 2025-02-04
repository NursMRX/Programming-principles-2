class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
account = Account(input("Owner is: "), abs(float(input("The balance is:"))))

account.deposit(float(input("Write the amount you want to deposit: ")))

account.withdraw(float(input("Write the amount you want to withdraw: ")))