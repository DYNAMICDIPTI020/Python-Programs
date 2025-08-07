import sys

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"  # Default PIN

    def authenticate(self):
        for _ in range(3):
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("Authentication successful.\n")
                return True
            else:
                print("Incorrect PIN.")
        print("Too many incorrect attempts. Exiting.")
        return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully.\n")
            else:
                print("Invalid amount.\n")
        except ValueError:
            print("Invalid input.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.\n")
            elif amount > self.balance:
                print("Insufficient balance.\n")
            else:
                print("Invalid amount.\n")
        except ValueError:
            print("Invalid input.\n")

    def change_pin(self):
        old_pin = input("Enter current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin and new_pin != "":
                self.pin = new_pin
                print("PIN changed successfully.\n")
            else:
                print("PINs do not match or invalid PIN.\n")
        else:
            print("Incorrect current PIN.\n")

    def menu(self):
        while True:
            print("----- ATM Menu -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    atm = ATM(balance=10000)  # Initial balance
    if atm.authenticate():
        atm.menu()