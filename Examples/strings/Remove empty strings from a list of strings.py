# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new = []
print(type(str_list))
#new = str_list.filter('')
#print(new)
for i in str_list:
    if i:
        new.append(i)
print(new)
