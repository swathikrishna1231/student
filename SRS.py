class student:
    def __init__(self,roll,name,age,marks):
        self.roll=roll
        self.name=name
        self.age=age
        self.marks=marks
    def save(self):
        with open("tu.txt","a") as a:
         a.write(f"\nroll:{self.roll},name:{self.name},age:{self.age},marks:{self.marks}")
class view:
    def __init__(self):
       with open("tu.txt","r") as a:
          print(a.read())
print("1.Add details")
print("2.Read all records")
print("3.search")
n=input("enter a choice")
if n =="1":
   o=input("enter roll no")
   x=input("enter name")
   y=input("enter age")
   z=input("enter marks")
   f=student(o,x,y,z)
   f.save()
elif n=="2":
   z=view()

   
   



   
   