class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Current Balance:", self.balance)

name = input("Enter Account Holder Name: ")
acc = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        acc.withdraw(amt)

    elif choice == 3:
        print("Current Balance:", acc.balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


