"""
Write a python program that simulates a simple banking system. 
The program should allow users to 
- create an account
- deposit money
- withdraw money
- check their balance
Implement error handling for insufficient funds during withdrawal and invalid inputs.
"""
from models import Account


accounts = []

# for account in accounts:
#     print(account.iban, account.balance, Account.next_iban)
  
# print("After second account transfered money to first")
# accounts[1].withdraw(500)
# accounts[0].deposit(500)
# accounts[1].transfer(accounts[0], 5000)


def create_account():
    return Account(
        int(input("Starting Balance: "))
    )

def find_account(account_id):
    for account in accounts:
        if account.iban == account_id:
            return account
    return None


def display_user():
    account_id = int(input("Account ID: "))
    account = find_account(account_id)
    if account is not None:
        account.display()
    else:
        print(f"Account with ID {account_id} not found!")

while True:
    print("Available Commands:")
    print("\t1. create - [Create an account]")
    print("\t2. show <Accound ID> - [displays account details]")
    command = input(">>> ").lower()
    if command == "create":
        print("Creating Account ...")
        accounts.append(create_account())
    elif command == "show":
        display_user()
    elif command == "transfer":
        pass
    elif command == "deposit":
        pass
    elif command == "withdraw":
        pass
    else:
        print("Command not found!")
