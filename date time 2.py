# Python strftime()
import datetime as dt
d1 = dt.date(2013,5,22)
print(d1)
print("strftime method :" ,d1.strftime("%d:%m:%Y"))
t1 = dt.datetime.now()
print("current time in strftime method :",t1.strftime('%H:%M:%S'))
d_t = dt.datetime.today()
print("current date and time ",d_t.strftime("%d:%b:%Y , %H:%M%p"))



# Python strptime()
# The strptime() method creates a datetime object from the given string.

uk_d = "12/10/2013"
print(uk_d)
uk_obj = dt.datetime.strptime(uk_d, "%m/%d/%Y")
print("changed date formate ",uk_obj)

print(dt.date.today())
print(dt.date.today().strftime("%d/%B/%Y"))