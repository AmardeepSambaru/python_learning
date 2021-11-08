#ex 1

def sam():
    print("hello")
    print('how are you')
sam()

#Ex 2
def sam(name):
    print('hello',name)
    print('how are you ?')
sam("Amar")

#Ex 3

def addition_val(n1,n2):
    result = n1 + n2
    return result
number1 = 5.5
number2 = 7.5
result = addition_val(number1,number2)
print("the sum is : ",result)

#Ex 4

def addition_val(n1,n2):
    result = n1 + n2
    return result

n1 = 5.5
n2 = 7.5
result = addition_val(n1,n2)
print("the sum is : ",result)

#Ex 5
def value(numbers):
    total_sum = sum(numbers)
    avarage_value = total_sum / len(numbers)
    return avarage_value

def grade_of(total_marks):

    if total_marks >= 80:
        grade = 'A'
    elif total_marks >= 70:
        grade = 'B'
    elif total_marks >= 55:
        grade = 'C'
    elif total_marks >= 35:
        grade = 'D'
    else:
        grade = 'D'
    return grade

marks = [50,60,70,59,78,80]

avarage_value = value(marks)

print("avarage value is " , avarage_value)

grade = grade_of(avarage_value)

print('your grade is ', grade)

