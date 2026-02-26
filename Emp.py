class Employee:
    def __init__(self,emp_id,emp_name,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.salary=salary
    def display(self):
        return f"emp_id:{self.emp_id},emp_name:{self.emp_name},salary:{self.salary}"
e1=Employee(1234,'Akhila',200000)
e2=Employee(2345,"Gautham",10000)
print(e1.display())
    