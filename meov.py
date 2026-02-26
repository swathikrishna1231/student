class student:
    def display(self,name,age=None):
        if age==None:
            return name
        else:
            return age
obj=student()
print(obj.display("swathi"))
print(obj.display("swathi",23))

         


