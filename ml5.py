class student:
    def __init__(self,rollno):
        self.rollno=rollno
class marks(student):
    def __init__(self, rollno,markss):
        super().__init__(rollno)
        self.markss=markss
class result(marks):
    def __init__(self,rollno,markss):
        super().__init__(rollno,markss)
    def display(self):
        return f"rn:{self.rollno}\nmr:{self.markss}"
a1=result(21,25)
print(a1.display())