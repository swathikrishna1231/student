class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"name:{self.name},age:{self.age}"
p1=Person("swathi",27)
p2=Person("katy",25)
print(p1.display())