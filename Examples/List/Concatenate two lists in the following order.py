# Concatenate two lists in the following order
# Expected output:
#
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

for i in list1:
    for j in list2:
        print(i+j, end=' ')

# another method

new = [i + j for i in ['hello','take'] for j in ['dear','sir']]
print('\n',new)


