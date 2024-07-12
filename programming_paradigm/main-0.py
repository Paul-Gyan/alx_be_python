# main-0.py

from bank_account import BankAccount
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> <amount>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0

    my_account = BankAccount(initial_balance=1000)

    if operation == 'deposit':
        my_account.deposit(amount)
    elif operation == 'withdraw':
        my_account.withdraw(amount)
    elif operation == 'balance':
        my_account.display_balance()
    else:
        print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")

if __name__ == "__main__":
    main()