class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class car(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def display(self):
        print("drive")
class boat(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def display(self):
        print("sail")
class flight(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def display(self):
        print("fly")
car1=car("jaguar",123)
boat1=boat("gombu",321)
flight1=flight("jomu","lalal")
for x in (car1,boat1,flight1):
    print(x.brand)
    print(x.model)
    x.display()