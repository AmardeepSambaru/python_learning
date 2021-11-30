# Python Program to Find the Largest Among Three Numbers

n = [111,879,548,]
if (n[0]>n[1]) and (n[0]>n[2]):
    largest = n[0]
elif (n[1]>n[0]) and (n[1]>n[2]):
    largest = n[1]
else :
    largest = n[2]
print("the largest number is :",largest)

# user input

n1 = int(input("enter the number :"))
n2 = int(input("enter the number :"))
n3 = int(input("enter the number :"))

if (n1>n2) and (n1>n3):
    largest = n1
elif (n2>n1) and (n2>n3):
    largest = n2
else :
    largest = n3
print("the largest number is :",largest)