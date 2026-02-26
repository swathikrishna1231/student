from abc import ABC, abstractmethod

class Shape(ABC):  
        @abstractmethod
        def area(self):   
             pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

s = Square(4)
r = Rectangle(5, 3)

print("Square Area:", s.area())
print("Rectangle Area:", r.area())
