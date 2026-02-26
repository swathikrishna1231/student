from time import sleep
from threading import *


class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(0.5)


class hai(Thread):
    def run(self):
        for i in range(5):
            print('Hai')
            sleep(0.5)

obj1=hello()
obj2=hai()
 
obj1.start()
sleep(0.5 )
obj2.start()

obj1.join()
obj2.join()

print("bye")