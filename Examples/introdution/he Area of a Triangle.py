# Python Program to Calculate the Area of a Triangle
b = 10
h = 25
area_triangle = (b*h)*0.5
print(area_triangle)

def area():
    b = int(input("enter the value : "))
    h = int(input("enter the value : "))
    result = (b*h)*0.5
    return result
tri_area = area()
print("Area of triangle :",tri_area)
