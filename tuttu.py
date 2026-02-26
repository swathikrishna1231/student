class fruits:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def __str__(self):
        return f"name:{self.name},colour:{self.colour}"

item1=fruits("apple","red")
item2=fruits("mango","yellow")
item3=fruits("grape","violet")
print(item1)
print(item2)
print(item3)
