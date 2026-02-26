class vehicle:
    def __init__(self,brand):
        self.brand=brand
class car(vehicle):
    def display(self):
        print(self.brand)
c=car("toyota")
print(c.display())
