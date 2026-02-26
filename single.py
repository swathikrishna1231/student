class animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
class dog(animal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def dis(self):
        return f"Dog:{self.name} Type:{self.type}"
class cat(animal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def dis(self):
        return f"Cat:{self.name} Type:{self.type}"
g=dog("Archana","Bad")
c=cat("Akhila","Very bad")
print(g.dis())
print(c.dis())
