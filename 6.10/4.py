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

account = None
account_2 = create_account(0)

while(True):
    command = None
    command = input(
        "\nвведите\n" \
        "1 (создать счет)\n" \
        "2 (пополнить баланс)\n" \
        "3 (списать со счета)\n" \
        "4 (проверить баланс)\n" \
        "5 (перевести на account_2): ")

    if command not in "12345":
        print("вводите только 1, 2, 3, 4 или 5!")
        continue
    command = int(command)

    if account == None and command != 1:
        print("сначала создайте счет!")
        continue
    elif account != None and command == 1:
        print("Счет уже создан!")    
        continue

    if command == 1:
        account = create_account(0)
    if command == 2:
        try:
            amount = int(input("Введите сумму: "))
            account.increase_balance(amount)
        except:
            print("Сумма должны быть числом!")
    if command == 3:
        try:
            amount = int(input("Введите сумму: "))
            account.decrease_balance(amount)
        except:
            print("Сумма должны быть числом!")
    if command == 4:
        account.check_balance()
    if command == 5:
        try:
            amount = int(input("Введите сумму: "))
            account.transfer(amount, account_2)
        except:
            print("Сумма должны быть числом!")
        
