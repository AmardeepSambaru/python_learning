# Display Fibonacci series up to 10 terms
n1 = 0
n2 = 1
for i in range(10):
    #print("the i is :",i)
    print(n1,end=' ')
    fib = n1 + n2
    n1 = n2
   # print("n1 is :",n1)
    n2 = fib
    #print(fib)
    #print("n2 is :",n2)


