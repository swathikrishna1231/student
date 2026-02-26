class tax_processor:
    def calculate(self,amount):
        pass
    def get_total_bill(self,amount):
        tax=self.calculate(amount)
        return amount+tax

class USA(tax_processor):
    def __init__(self,stat_rate):
        self.stat_rate=stat_rate
    def calculate(self,amount):
        return amount * self.stat_rate
         
class UK(tax_processor):
    def calculate(self,amount):
        return amount*0.20
class India(tax_processor):
    def __init__(self,gst_category):
        self.gst_category=gst_category
    def calculate(self,amount):
        if self.gst_category=="luxuary":
             return amount*0.28
        else:
            return amount*0.18
amount=1000
usa=USA(0.04)
uk=UK()
india=India("")
print("USA:",usa.get_total_bill(amount))
print("UK",uk.get_total_bill(amount))
print("india",india.get_total_bill(amount))



         

    



    
        