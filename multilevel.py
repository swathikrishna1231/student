class bank:
    def __init__(self,User_name,Account_No):
        self.User_name=User_name
        self.Account_No=Account_No
class details(bank):
    def __init__(self,User_name,Account_No,balance):
        super().__init__(User_name,Account_No)
        self.balance=balance
class operation(details):
    def __init__(self,User_name,Account_No,balance):
        super().__init__(User_name,Account_No,balance)
    def display(self):
        return f"name:{self.User_name},acno:{self.Account_No},balance:{self.balance}"
a1=operation("swathi",1234567,5000)
print(a1.display())



    
