import datetime as dt

today = dt.date.today()
print(today)

date1 = dt.date(2021, 6, 24)
print(date1)
print("year : ", date1.year)
print("month : ", date1.month)
print("date : ", date1.day)

time1 = dt.time(15, 0, 33)
print(time1)
print("hours : ", time1.hour)
print("minutes : ", time1.minute)
print("seconds : ", time1.second)

date_time = dt.datetime(2021, 10, 25, 15, 54, 33, 22222)
print(date_time)
'''
print("year : ",date_time.year)
print("month : ", date_time.month)
print("date : ",date_time.day)

print("hours : ",date_time.hour)
print("minutes : ",date_time.minute)
print("seconds : ",date_time.second)'''

current = dt.datetime.now()
print(current)

next = dt.datetime(2022, 1, 1, 0, 0, 0, )
diff = next - current
print(diff)
print(type(diff))

t1 = dt.timedelta(12, 0, 0)
t2 = dt.timedelta(11, 8, 00)
t3 = t1 - t2
print(t3)
