# Remove empty strings from the list of strings

# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Use a filter() function to remove the None / empty type from the list
new = list(filter(None,list1))
print(new)

for i in list1:
    if i:
        print(i,end=' ')