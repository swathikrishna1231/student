class bird:
    def sound(self):
        print("chirp")
class cat:
    def sound(self):
        print("Meow")
b1=bird()
c1=cat()
for i in (b1,c1):
    (i.sound())
