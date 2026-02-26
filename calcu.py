class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
calc=Calculator(2,5)
clac=Calculator(80,20)
print(calc.add())
print(clac.sub())