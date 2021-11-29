'''class student:
    def pass_fail(self):

        if self.marks <40 :
            return False
        else:
            return True

student1 = student()
student1.name = "Amar"
student1.marks = 75
did_he_pass = student1.pass_fail()
print(did_he_pass)

student2 = student()
student2.name = "Raghu"
student2.marks = 40
did_he_pass = student2.pass_fail()
print(did_he_pass)

student3 = student()
student3.name = "shiva"
student3.marks = 35
did_he_pass = student3.pass_fail()
print(did_he_pass)'''


class student:
    def pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age


student1 = student("amar", 85, 15)
student2 = student("raghu", 35, 14)
print("student1 name is :", student1.name)
print("student1 marks is :", student1.marks)
print("student1 age is :", student1.age)
did_he_pass = student1.pass_fail()
print("student1 is pass :", did_he_pass)
did_he_pass = student2.pass_fail()
print("student2 is pass :", did_he_pass)



class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def tri_peremetr(self):
        result = self.a +self.b + self.c
        return result

t1 = triangle(3,4,5)
pere_meter = t1.tri_peremetr()
print("the perimeter of t1 triangle is :" , pere_meter)
print(isinstance(t1,triangle))



