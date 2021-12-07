# Create a function with default argument

# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# output = Name: Ben salary: 12000
#          Name: Jessa salary: 9000

#salary = 9000
def show_employee(name,salary = 9000):
    print(name,"salary is :",salary)

result1 = show_employee("radhu",12000)
result2 = show_employee("shiva")
print(result1)
print(result2)