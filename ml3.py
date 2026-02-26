class Account:
    def __init__(self,account_no):
        self.account_no=account_no
    def show_account(self):
        return f"ac:{self.account_no}"
class SavingsAccount(Account):
    def __init__(self,account_no,balance):
        super().__init__(account_no)
        self.balance=balance
    def show_bal(self):
        return f"ac:{self.account_no}\n balance:{self.balance}"
class interestac(SavingsAccount):
    def __init__(self,account_no,balance,interest_rate):
        super().__init__(account_no,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        return(self.balance*self.interest_rate)/100
    def display(self):
        interest=self.calculate_interest
        return f"ac:{self.account_no},balance:{self.balance},interest :{interest}"
a1=interestac(1234,5000,10)
print(a1.display())

        
        