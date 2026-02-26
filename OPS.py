from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    def payment_success():
        print("payment completed successfully")
class creditcardpayment(payment):
    def pay(self,amount):
        self.amount=amount
        print(f"processing credit card{self.amount}")
class UPIpayment(payment):
    def pay(self,amount):
        self.amount=amount
        print(f"procesing UPIpayment{self.amount}")
class Netbanking(payment):
    def pay(self,amount):
        self.amount=amount
        print(f"processing netbanking payment{self.amount}")

b=UPIpayment()
b.pay(1000)
b.payment_success



     

        
