class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def mark(self):
        if self.marks>=40:
            return "pass"
        else:
            return "fail"
stu1=student("swathi",21,41)
stu2=student("akhila",20,60)
stu3=student("gautham",25,30)
stu4=student("archana",16,60)
print(stu3.mark())
