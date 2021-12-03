'''
try:
    a = int(input("enter the possitive value : "))
    if a <=0:
        raise ValueError("your not entered possitive value : ")
except ValueError as ve:
    print(ve)
    print("in except")
#print("your entered correct value")


try:
    num = int(input("enter the number :"))
    assert num %2 ==0
except:
    print("you entered add number")
else:
    reciprocal = 1/num
    print(reciprocal)'''
import sys

'''
class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

#from sys import exit

number = 10
while True:
    try:
        i_num = int(input("enter the value: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("this value is too small , try again ")
        #sys.exit()
       # print()
    except ValueTooLargeError:
         print("the value is too large, try again  ")
         print()

print("you gussed correct value")'''
'''
class maths():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def addition(self):
        result1 = self.a + self.b + self.c
        return result1

    def multiply(self):
        result2 = self.a * self.b * self.c
        return result2


add_value = maths(10,20,30)
sum1 = add_value.addition()
print("the addition of values ",sum1)

sum2 = add_value.multiply()
print("the multiplication of the values :",sum2)'''
'''
class maths:
    def addition_1(self,a,b,c):

        result1 = a + b + c
        print(a)
        return result1

addition1_value = maths()
#addition1_value.a = 15
#addition1_value.b = 25
#addition1_value.c = 35
sum1 = addition1_value.addition_1(12,50,60)
print(sum1)
isinstance(addition1_value,maths)'''

'''
from barcode import EAN13
n = '489745612302'
co = EAN13(n)
co.save("bar_code")'''

'''
class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x,y)


p1 = point(1, 2)
p2 = point(3, 4)
print(p1+p2)'''


# polymorphsim

class animals:

    def walk(self):
        print("animals can walk")

    def talk(self):
        print("animals cannot talk")

    def swim(self):
        print("animals can also swim")


class bird:

    def walk(self):
        print("birds can walk")

    def swim(self):
        print("birds cannot swim")

dog = animals
parrot = bird

for nature in (animals,bird):
    nature.walk(1)
    nature.swim(1)
    nature.talk(1)
