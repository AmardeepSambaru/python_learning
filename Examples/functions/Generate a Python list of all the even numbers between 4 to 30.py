# Generate a Python list of all the even numbers between 4 to 30
# Expected Output:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

new_list = []
def even_num():
    for i in range(4,30):
        if i %2 ==0:
            new_list.append(i)
print(even_num())
print(new_list)
