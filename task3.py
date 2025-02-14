class BankAccount:
    def __init__(ba, account_number, owner, balance=0):
        ba.account_number = account_number
        ba.owner = owner
        ba.balance = balance

    def deposit(ba, amount):
        ba.balance += amount
        print(f"Deposited: ₱{amount:.2f}")

    def withdraw(ba, amount):
        if amount <= ba.balance:
            ba.balance -= amount
            print(f"Withdrew: ₱{amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(ba):
        print(f"Account Balance: ₱{ba.balance:.2f}")


account = BankAccount("123456789", "Hance Balintong", 1000)

account.display_balance()

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
account.display_balance()

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display_balance()
