class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, amount, recepient):
        self.balance -= amount
        recepient.balance += amount
    
    def increase_balance(self, amount):
        self.balance += amount

    def decrease_balance(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"Ваш баланс = {self.balance}")

def create_account(initial_balance):
    return BankAccount(initial_balance)

account_1 = create_account(100)

account_1.decrease_balance(10)
account_1.check_balance()

