class animals:

    def eat(self):
        print("i can eat")
    def swim(self):
        print("i can swim in water")

class dog(animals):
    #def bark(self):
        print()
dog1 = dog()
dog1.eat()

class fish(animals):
    def walk(self):
        print("i canot walk")
fish1 = fish()
fish1.eat()
fish1.swim()


class rajam:
    def __init__(self):
        print()

    def marriage_status(self):
        print(" is married")
    def marriage_status1(self):
        print(" is not married")

class devarajam(rajam):
    print()

srinivas = devarajam()
shekar = devarajam()
raviteja = devarajam()
amardeep = devarajam()

amardeep.marriage_status1()

import os
#os. mkdir('Examples')
os.mkdir('Examples/introdution')