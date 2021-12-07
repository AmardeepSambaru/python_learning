# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
str1 = input("enter the word with number : ")
new = []
print(type(str1))
result = str1.split()
print(result)
for i in result:
    if i.isdigit():
        print(i)


