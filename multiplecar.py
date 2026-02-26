class engine:
    def __init__(self,engine_type):
        self.engine_type=engine_type
class brand:
    def __init__(self,brand_name):
        self.brand_name=brand_name
class car(engine,brand):
    def __init__(self,engine_type,brand_name,price):
        engine.__init__(self,engine_type)
        brand.__init__(self,brand_name)
        self.price=price
    def dispaly(self):
        return f"eg:{self.engine_type},br:{self.brand_name},pr;{self.price}"
    
a1=car("v5engine","jaguar",15000000)