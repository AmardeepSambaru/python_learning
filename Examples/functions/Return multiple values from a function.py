# Return multiple values from a function


# Write a program to create function calculation() such that it can accept two variables
# and calculate addition and subtraction. Also,
# it must return both addition and subtraction in a single return call.

def calculation(a,b):
    result1 = a + b
    result2 = a - b
    return result1 , result2
finall = calculation(40,10)
print(finall)