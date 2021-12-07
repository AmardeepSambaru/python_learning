# Assign a different name to function and call it through the new name
# Below is the function display_student(name, age).
# Assign a new name show_tudent(name, age) to it and call it using the new name.

def class_student(name,age):
    print("student name is :",name,"and the age is:",age)

new_class = class_student
info = new_class("karthik",25)
print(info)