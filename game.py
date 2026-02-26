class knight:
    def attack(self):
        print("knight swings a sword")
class Archer:
    def attack(self):
        print("archer shoots an arrow")
class robot:
    def attack(self):
        print("robot fires using machine gun")
def startfighter(fighter):
    fighter.attack()
k=knight()
a=Archer()
r=robot()
startfighter(k)
startfighter(a)
startfighter(r)