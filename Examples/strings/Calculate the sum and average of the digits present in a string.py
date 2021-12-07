# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum
# and average of the digits that appear in the string, ignoring all other character

str1 = "PYnative29@#8496"
new = []
for i in str1:
    if i.isdigit():
        new.append(int(i))
print(new)
print(type(new))
result1 = sum(new)
print("sum of the all digits in str1: ",result1)
result2 = result1 / len(new)
print("avarage value of digit present in str1 : ",result2)



