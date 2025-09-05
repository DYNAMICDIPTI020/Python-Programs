class Account:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_statement(self):
        return self.transactions[-10:]  # Last 10 transactions

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_account_number = 1001
    
    def create_account(self, name, initial_balance=0):
        account_number = self.next_account_number
        self.accounts[account_number] = Account(account_number, name, initial_balance)
        self.next_account_number += 1
        return account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_account, to_account, amount):
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)
        
        if from_acc and to_acc and from_acc.withdraw(amount):
            to_acc.deposit(amount)
            from_acc.transactions.append(f"Transferred ${amount} to {to_account}")
            to_acc.transactions.append(f"Received ${amount} from {from_account}")
            return True
        return False

# Example usage functions
def demo():
    bank = Bank("Python Bank")
    
    # Create accounts
    acc1 = bank.create_account("Alice", 1000)
    acc2 = bank.create_account("Bob", 500)
    
    print(f"Created accounts: {acc1}, {acc2}")
    
    # Banking operations
    alice = bank.get_account(acc1)
    bob = bank.get_account(acc2)
    
    alice.deposit(200)
    bob.withdraw(100)
    bank.transfer(acc1, acc2, 150)
    
    print(f"Alice balance: ${alice.get_balance()}")
    print(f"Bob balance: ${bob.get_balance()}")
    print(f"Alice transactions: {alice.get_statement()}")

if __name__ == "__main__":
    demo()