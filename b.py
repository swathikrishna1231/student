class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def __init__(self,name):
        super().__init__(name)
    def display(self):
        return f"name:{self.name}"
a1=dog("jaanu")
a2=dog("neethu")
print(a2.display())

hhhhh
hhhhh
hhhhhh
