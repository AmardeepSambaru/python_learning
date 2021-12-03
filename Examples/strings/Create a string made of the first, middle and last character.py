# Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s
# first, middle, and last character
'''
new_name = str()
name = input("enter the name :")
print(name)
print(type(name))
new_name = name[0]+name[2]+name[4]
print(new_name)'''


name1 = input("enter the name :")
first = name1[0]
total_len = len(name1)
middle_cha = int(total_len / 2)
last_cha = total_len - 1
print(first + name1[middle_cha] + name1[last_cha])

# Write a program to create a new string
# made of the middle three characters of an input string

user = input("enter the name :")
tot = len(user)
midd = int(tot / 2)
three = midd + 1
four = midd -1
variable = user[four] + user[midd] + user[three]
print("middle three characters:",variable)

