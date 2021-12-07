operation = input("enter the value with expresion : ")
print(type(operation))
spl = operation.split(" ")
print(spl)
print(spl[1])

if spl[1] == "+":
    print(int(spl[0]) + int(spl[2]))

elif spl[1] == "-":
    print(int(spl[0]) - int(spl[2]))

elif spl[1] == "/":
    print(int(spl[0]) / int(spl[2]))

#print(operation)




