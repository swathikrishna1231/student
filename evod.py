from threading import *
from time import *
class even(Thread):
    def run(self):
        for i in range(1,11):
            if i%2==0:
                print(i)
                sleep(1)
class odd(Thread):
    def run(self):
        for i in range(1,11):
            if i%2!=0:
                print(i)
                sleep(1)

ev=even()
od=odd()
od.start()
ev.start()
ev.join()
od.join()

