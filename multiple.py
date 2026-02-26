class father:
    def __init__(self,name):
        self.name=name
class mother:
    def __init__(self,mother_name):
        self.mother_name=mother_name
class child(father,mother):
    def __init__(self,name,mother_name):
        father.__init__(self,name)
        mother.__init__(self,mother_name)
    def display(self):
        return f"name:{self.name},mom_name:{self.mother_name}"
a1=child("shyam","shyama")
a2=child("roy","amina")
a3=child("abdulla","parvathy")
print(a3.display())