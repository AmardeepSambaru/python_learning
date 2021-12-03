# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
char = 0
digits = 0
symbols = 0
for i in str1:
    if i.isalpha():
        #char.append(i)
        char +=1
    elif i.isdigit():
        #digits.append(i)
        digits +=1
    else:
        #symbols.append(i)
        symbols +=1

print("char = ",char,"digits =",digits , "symbols = ",symbols)

