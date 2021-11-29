name = ['amar','deep','ravi','teja','raja','shekar',
        'srinivas','sai','vijaya','sambaru']
#ex for break

for i in name:
    if i == 'teja':
        break
    print(i)
print('the end')

# ex for continue

for i in name:
    if i =='shekar':
        continue
    if i =='vijaya':
        continue
    print(i)


