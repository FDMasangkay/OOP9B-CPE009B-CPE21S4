"""
    ATM.py
"""

class ATM:
    def __init__ (self, serial_number = 0, account = None, amount = 0):
        self.serial_number = serial_number
        self.account = account
        self.amount = amount

    def deposit(self, amount):
        self.account.current_balance = self.account.current_balance + amount
        self.account.transaction_history.append(f"Deposited ${amount}")
        print("Deposit Complete")

    def withdraw(self, amount):
        self.account.current_balance = self.account.current_balance - amount
        self.account.transaction_history.append(f"Withdrew ${amount}")
        print("Withdraw Complete")

    def check_current_balance(self):
        print (self.account.current_balance)  

    def view_transactionsummary (self):
        print("Transaction Summary")
        print("Account Number: ", self.account.account_number)
        print("Account Name: ", self.account.account_firstname, self.account.account_lastname)
        print("Current Balance: ", self.account.current_balance)
        print("Transaction History:")
        for transaction in self.account.transaction_history:
            print(transaction)

