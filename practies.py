#Find triangle Area

def value(a,b):
    area = (a*b)*0.5
    return area
#user enter the values one by one

area = value(int(input("enter the height :")),int(input("enter the base :")))
print("the triangle area is ",area)

#find rectangle peremeter

def rectangle(l,w):
    peremeter = 2*(l+w)
    return peremeter
peremeter = rectangle(int(input("enter the length :")),int(input("enter the width :")))
print("rectangle peremeter is ",peremeter)

import sys
li = ['a', 0, 2]
for i in li:
    try:
        print("the entery is", i)
        r = 1 / int(i)
        break
    except:
        print("oops!", sys.exc_info()[0], "occurred.")
        print("next entery")
        print()
print("the reciprocal of" ,i ,"is" ,r)




