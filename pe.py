class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(person):
    def __init__(self,name,age,rollno,mark):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def __str__(self):
        return f"{self.name}\n{self.rollno}"
a1=student("swathi",25,20,50)
print(a1)