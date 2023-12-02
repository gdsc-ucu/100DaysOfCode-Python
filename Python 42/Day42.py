class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_holder, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        self.deposit(interest)
        print(f"Interest calculated and deposited: ${interest}")


if __name__ == "__main__":

    account1 = BankAccount("John Wick", 1000)
    savings_account1 = SavingsAccount("Jane Wick", 5000, 0.05)

    # Depositing and withdrawing money from the accounts
    print("John Wick's account;")
    account1.deposit(500)
    account1.withdraw(200)
    print("\n")
    print("John Jane's savings account;")
    savings_account1.deposit(1000)
    savings_account1.withdraw(300)

    savings_account1.calculate_interest()

    print("\n")
    print(f"{account1._account_holder}'s final balance: ${account1.get_balance()}")
    print(f"{savings_account1._account_holder}'s final balance: ${savings_account1.get_balance()}")