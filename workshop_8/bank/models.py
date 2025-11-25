class Account:
    # static attributes
    next_iban = 1
    def __init__(self, starting_balance = 0):
        self.balance = starting_balance
        self.iban = Account.next_iban
        Account.next_iban += 1

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds!")
        if amount <= 0:
            raise ValueError("Withdrawal amount should be only positive number!")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposited amount should be only positive number!")
        self.balance += amount

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)

    def display(self):
        print(f"Displaying Account {self.iban}")
        print(f"\tBalance: {self.balance}")
