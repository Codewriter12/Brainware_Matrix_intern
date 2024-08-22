class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append(f"Checked balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
            self.transaction_history.append(f"Deposited: ₹{amount}")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
            self.transaction_history.append(f"Withdrew: ₹{amount}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Enter a valid amount to withdraw.")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

def atm_interface():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)
        elif choice == '4':
            atm.view_transaction_history()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_interface()
