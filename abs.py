from abc import ABC, abstractmethod
class school(ABC):
    @abstractmethod
    def tea(self,sub):
        pass
    def clas(self,sub):
        return f"teacher{self.sub}go the class"
    
class maths(school):
    def tea(self,sub):
        self.sub=sub
        return f"{self.sub} teacher is swathi"
class science(school):
    def tea(self,sub):
        self.sub=sub
        return f"{self.sub}teacher is archana"
class ss(school):
    def tea(self,sub):
        self.sub=sub
        return f"{self.sub}teacher is akhila"

a=input("enter the sub").lower()
if a==maths:
    



