class car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def __str__(self):
        return f"brand:{self.brand},year:{self.year}"
item1=car("ambassdor","1956")
item2=car("honda","2000")
item3=car("jaguar","2016")
print(item3)
