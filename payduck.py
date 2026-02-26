class UPI:
    def pay(self):
        return "payment done through UPI"
class creditcard:
    def pay(self):
        return "payment done through credit card"
class Netbanking:
    def pay(self):
        return "payment done through netbanking"
def payment(paid):
    print(paid.pay())
u=UPI()
c=creditcard()
n=Netbanking()
d=input('enter choice')
print('1.UPI')  
print("2.credit card")
print("3.Netbanking")
if d=="1":
    payment(u)
elif d=="2":
    payment(c)
else:
    payment(n)
    

