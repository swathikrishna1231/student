class PersonalInfo:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        return f"name:{self.name}"
class JobInfo:
    def __init__(self,salary):
        self.salary=salary
    def show_salary(self):
        return f"salary:{self.salary}"
class employee(PersonalInfo,JobInfo):
    def __init__(self,name,salary,emp_id):
        PersonalInfo.__init__(self,name)
        JobInfo.__init__(self,salary)
        self.emp_id=emp_id
    def display(self):
        return f"name:{self.name}\nsalary:{self.salary}\nemp_id:{self.emp_id}"
a1=employee("swathi",50000,1234)
print(a1.display())





