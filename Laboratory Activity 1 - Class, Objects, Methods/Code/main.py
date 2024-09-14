"""
    Main.py
"""

import Accounts
import ATM
import random

# create the instance/object
Account1 = Accounts.Accounts( 
account_number =123456,
account_firstname = "Royce",
account_lastname = "Chua",
current_balance = 1000,
address = "Silver Street Quezon City",
email = "roycechua123@gmil.com"
)

print ("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

# create the instance/object
Account2 = Accounts.Accounts( 
account_number = 654321,
account_firstname = "John",
account_lastname = "Doe",
current_balance = 2000,
address = "Gold Street Quezon City",
email = "Johndoe@yahoo.com"
)
print ("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

print()

# creating and Using ATM object
ATM1 = ATM.ATM(serial_number = random.randrange(10**5, 10**6), account=Account1)
ATM1.deposit(500)
print(f"Current Balance: {ATM1.check_current_balance()}")
ATM1.deposit(300)
print(f"Current Balance: {ATM1.check_current_balance()}")
ATM1.deposit(200)
print(f"Current Balance: {ATM1.check_current_balance()}")
ATM1.deposit(200)
ATM1.deposit(200)

ATM2 = ATM.ATM(serial_number = random.randrange(10**5, 10**6), account=Account2)
ATM2.deposit(300)
print(f"Current Balance: {ATM2.check_current_balance()}")

print("Serial Number:")
print(ATM1.serial_number)

ATM1.view_transactionsummary()
ATM2.view_transactionsummary()