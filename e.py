class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
class manager(employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name, emp_id)
        self.department=department
    def display(self):
        return f"name:{self.name}\nemp_id:{self.emp_id}\n department:{self.department}"
a1=manager("SWathi","1","BSW")
print(a1.display())

    

    