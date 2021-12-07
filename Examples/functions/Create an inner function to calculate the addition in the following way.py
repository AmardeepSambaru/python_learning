# Create an inner function to calculate the addition in the following way


# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def math(a,b):
    def addition():
        result1 = a + b
        return result1
    total = addition()
    return total + 5
s = math(10,20)
print(s)


