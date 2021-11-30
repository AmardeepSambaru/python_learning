class vehicle:
    def __init__(self,name,speed,milege,capacity):
        self.name = name
        self.speed = speed
        self.milege = milege
        self.capacity = capacity
    def fare(self):
        return self.capacity *100
class bus(vehicle):
    print()
rtc = bus("indra",110,17,35)
amount = rtc.fare()
print("the fare amount is :",amount)

print(type(rtc))
inst = isinstance(rtc,vehicle)
print(inst)