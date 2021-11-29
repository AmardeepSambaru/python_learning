for i in range(0,5):
    #print(i)
    num = 5
    for j in range(0,i+1):
        #print(j)
        print(num , end=' ')
        num = num-1
    print("\t")


name = "python"
for i in range(len(name)):
    for j in range(i+1):

        print(name[j] , end=' ')
    print()


for i in range(0,5):
    num = 1
    for j in range(0,i+1):
        print(num ,end=' ')
        num = num+1
    print()


for i in range(0,5):
    num = 1
    for j in range(5-i):
        print(num ,end=' ')
        num =num+1
    print()

for i in range(0,5):
    num = 5
    for j in range(5-i):
        print(num ,end=' ')
        num = num-1
    print()




