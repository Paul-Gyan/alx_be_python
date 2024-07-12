# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.current_balance = initial_balance

    def deposit(self, amount):
       
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.current_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount): 
        if amount > 0 and self.current_balance >= amount:
            self.current_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.current_balance:.2f}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
       
        print(f"Current balance: ${self.current_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    my_account = BankAccount(initial_balance=100)
    my_account.deposit(50)
    my_account.withdraw(20)
    my_account.display_balance()