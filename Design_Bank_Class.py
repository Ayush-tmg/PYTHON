# Open an account (fn, ln, age, balance = 0)
# Get Current Balance
# Deposit Balance
# Withdraw Balance
# Get Interest rate (12%)
# Print Government Holidays

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Account:
    def __init__(self, fn, ln, age, balance=0):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.balance = balance

    def get_current_balance(self):
        return self.balance

    def deposit_balance(self, amount):
        self.balance += amount

    def withdraw_balance(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_interest_rate(self):
        return 0.12

    def print_government_holidays(self):
        print("Government holidays in Nepal:")
        print("1. Republic Day (May 29)")
        print("2. Raksha Bandhan (August 31)")
        print("3. Maghe Sankranti (January 15)")

def open_account(fn, ln, age, balance=0):
    """Opens a new account for the given customer.

    Args:
        fn: First name of the customer.
        ln: Last name of the customer.
        age: Age of the customer.
        balance: Initial balance of the account.

    Returns:
        An Account object representing the new account.
    """

    account = Account(fn, ln, age, balance)
    return account

def main():
    # Open an account.
    account = open_account("John", "Doe", 30)

    # Get current balance.
    current_balance = account.get_current_balance()
    print(f"Current balance: {current_balance}")

    # Deposit balance.
    account.deposit_balance(1000)

    # Get current balance again.
    current_balance = account.get_current_balance()
    print(f"Current balance: {current_balance}")

    # Withdraw balance.
    account.withdraw_balance(500)

    # Get current balance again.
    current_balance = account.get_current_balance()
    print(f"Current balance: {current_balance}")

    # Get interest rate.
    interest_rate = account.get_interest_rate()
    print(f"Interest rate: {interest_rate}")

    # Print government holidays.
    account.print_government_holidays()

if __name__ == "__main__":
    main()
