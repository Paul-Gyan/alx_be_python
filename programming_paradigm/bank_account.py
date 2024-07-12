# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount instance.

        Args:
            initial_balance (float, optional): Initial account balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): Amount to deposit.

        Returns:
            None
        """
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.account_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if funds are sufficient.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            bool: True if successful, False if insufficient funds.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.account_balance:.2f}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        """
        Displays the current account balance.

        Returns:
            None
        """
        print(f"Current balance: ${self.account_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    my_account = BankAccount(initial_balance=1000)
    my_account.deposit(200)
    my_account.withdraw(150)
    my_account.display_balance()