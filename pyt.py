class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return f"name:{self.name},rollno:{self.rollno}"
slno1=student('swathi','50')
slno2=student('akhila','100')
slno3=student("gautham",'60')
print(slno2)