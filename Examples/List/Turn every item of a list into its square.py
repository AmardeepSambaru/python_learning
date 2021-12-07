# Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square

import math
numbers = [1, 2, 3, 4, 5, 6, 7]

for i in numbers:
    i = i**2
    print(i,end=' ')


new = [i**2 for i in numbers]
print('\n',new)
