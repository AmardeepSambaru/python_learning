# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string
# so that all lowercase letters should come first.

str1 = 'PyNaTive'
lower = []
upper = []
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
new = ''.join(lower + upper)
print("the result is : ",new)
