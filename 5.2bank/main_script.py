from bank_module import BankAccount

account_holder_name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_holder_name, initial_balance)

print(f"\nAccount Holder: {account.account_holder}")
print("Initial Balance:", account.check_balance())

withdraw_amount = float(input("Enter the withdrawal amount: "))
print(account.withdraw(withdraw_amount))

deposit_amount = float(input("Enter the deposit amount: "))
print(account.deposit(deposit_amount))

print("Updated Balance:", account.check_balance())
