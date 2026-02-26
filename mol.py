class Area:
    def calculate(self,a,b=None):
        if b==None:
            return a*2
        else:
            return a*b
calc=Area()
print(calc.calculate(2))
print(calc.calculate(3,4))