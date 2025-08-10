# Simple Banking System
class Account:
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited {amount}. New balance: {self.balance}")
		else:
			print("Invalid deposit amount.")

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			print(f"Withdrew {amount}. New balance: {self.balance}")
		else:
			print("Invalid or insufficient funds.")

	def show_balance(self):
		print(f"Account holder: {self.name}, Balance: {self.balance}")

def main():
	accounts = {}
	while True:
		print("\n--- Banking System Menu ---")
		print("1. Create Account")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Show Balance")
		print("5. Exit")
		choice = input("Enter your choice: ")

		if choice == '1':
			name = input("Enter account holder name: ")
			if name in accounts:
				print("Account already exists.")
			else:
				accounts[name] = Account(name)
				print("Account created.")
		elif choice == '2':
			name = input("Enter account holder name: ")
			if name in accounts:
				amount = float(input("Enter amount to deposit: "))
				accounts[name].deposit(amount)
			else:
				print("Account not found.")
		elif choice == '3':
			name = input("Enter account holder name: ")
			if name in accounts:
				amount = float(input("Enter amount to withdraw: "))
				accounts[name].withdraw(amount)
			else:
				print("Account not found.")
		elif choice == '4':
			name = input("Enter account holder name: ")
			if name in accounts:
				accounts[name].show_balance()
			else:
				print("Account not found.")
		elif choice == '5':
			print("Exiting...")
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()
