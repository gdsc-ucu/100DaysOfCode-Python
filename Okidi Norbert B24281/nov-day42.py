class BankAccount:
    def __init__(self, account_name, balance = 0):
        self.account_name = account_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"{self.account_name} Desposited: UGX {amount} New balance: {self.balance}"
    
            
    
    def withdraw(self, amount):
        balance = self.balance
        if amount > balance:
            return "Insufficient funds!"
        
        
        else:
            self.balance -= amount
            return f"{self.account_name} Withdrew: UGX {amount} New balance: UGX {self.balance}"
            
    def get_balance(self):
        return f"Current Balance for {self.account_name}: UGX {self.balance}"

class SavingAccount(BankAccount):
    def __init__(self, account_name, balance = 0, interest_rate = 0.03):
        super().__init__(account_name, balance)
        self.interest_rate = interest_rate

    def interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"New balance: UGX {self.balance} with interest of UGX {interest}"
    


Norbert_account = BankAccount("Norbert")
print(Norbert_account.deposit(150000))

Norbert_account = BankAccount("Norbert",150000 )
print(Norbert_account.withdraw(5000))


print("\nTOTAL SAVINGS")
savingAccount = SavingAccount("Okidi", 20000)
print(savingAccount.get_balance())

print("\nDEPOSIT")
balance = savingAccount.deposit(10000)
print(balance)

print("\nINTEREST")
balance = savingAccount.interest()
print(balance)


