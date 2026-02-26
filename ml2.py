class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no=roll_no
class collegestudent(student):
    def __init__(self,name,roll_no,course):
        super().__init__(name,roll_no)
        self.course=course
    def display(self):
        return f"name:{self.name}\nrollno:{self.roll_no}\ncourse:{self.course}"
a1=collegestudent("swathi",22,"BSW")
print(a1.display())


        