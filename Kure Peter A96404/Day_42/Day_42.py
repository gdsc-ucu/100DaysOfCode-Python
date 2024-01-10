# Encapsulation
class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            print("Amount must be greater than zero")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient Funds." 
        
    def getBalance(self):
        return f"Current balance: ${self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interestRate = 0.01):
        super().__init__(name, balance)
        self.interestRate = interestRate
        
    def calculateInterest(self):
        interest = self.balance * self.interestRate
        self.deposit(interest)
        return f"Interest Calculated and deposited: ${interest}"
    
# Instances
regularAccount = BankAccount("Martin Tyler")
print("Account Holder:",regularAccount.name)
print(regularAccount.deposit(21000))
print(regularAccount.withdraw(1000))
print(regularAccount.getBalance())
print()

savings_account = SavingsAccount("Alan Smith", interestRate=0.05)
print("Account Holder:", savings_account.name)
print(savings_account.deposit(50000))
print(savings_account.withdraw(50))
print(savings_account.calculateInterest())
print(savings_account.getBalance())