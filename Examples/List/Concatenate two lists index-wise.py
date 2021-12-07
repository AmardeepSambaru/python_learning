# Concatenate two lists index-wise


# Write a program to add two lists index-wise.
# Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element.
# any leftover items will get added at the end of the new list.

# Expected output:
# ['My', 'name', 'is', 'Kelly']


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i,j in zip(list1,list2)]
print(list3)

num1 = [9,4,9,2,9]
num2 = [9,9,1,4,6]
number = [i j for i,j in zip(num1,num2)]
print(number)