# Python Program to Check Leap Year
year = int(input("enter the year : "))
def leap():
    if (year %4)==0:
        if (year%100)==0:
            if(year%400)==0:
                print("{} this is leap year".format(year))
            else:
                print("{} this is not leap year".format(year))
        else:
            print("{} this is leap year".format(year))
    else:
        print("{} this is not leap year".format(year))

    return
leap()