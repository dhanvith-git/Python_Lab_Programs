class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)


# Main Program
name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        print("Thank you for using our bank service!")
        break

    else:
        print("Invalid choice. Please try again.")