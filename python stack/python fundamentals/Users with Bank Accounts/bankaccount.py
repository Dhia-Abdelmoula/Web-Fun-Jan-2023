class BankAccount:
    balance = 0
    int_rate = 0.01
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
        
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
        
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.int_rate*self.balance) + self.balance
        return self
    
class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info(self)
        return self
    
    

anis = User ("anis","anisghadhab@utctunisie.com")
print(anis.make_deposit(100))

# Trump = BankAccount (0.05, 1000)

# Tate = BankAccount (0.1, 500)

# Trump_Bankaccount.deposit(200).deposit(200).deposit(100).yield_interest().display_account_info()
# Tate.deposit(100).deposit(100).withdraw(1).withdraw(300).withdraw(50).withdraw(50).yield_interest().display_account_info()
