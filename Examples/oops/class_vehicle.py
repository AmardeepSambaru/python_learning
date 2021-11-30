# Write a Python program to create a Vehicle class
# with max_speed and mileage instance attributes.

class vehicle:
    color = "white"

    def __init__(self, name, max_speed, milege):
        self.name = name
        self.max_speed = max_speed
        self.milege = milege

    def seating_capacity(self, capacity):
        return f"the seating capacity of {self.name} is {capacity} passangers"


car = vehicle('bmw', 180, 27)
print("the max speed of car is {} and the color is {}:".format(car.max_speed, car.color))


# Create a child class Bus
# that will inherit all of the variables and methods of the Vehicle class

class bus(vehicle):
    print()


rtc = bus('indra', 100, 18)
print("the bus name is : ", rtc.name, "bus speed is :",
      rtc.max_speed, "milege is : ", rtc.milege)
print("the bus name is : {} \nand the bus speed is : {} "
      "\nthe bus milege is : {}\nthe bus color is :{}"
      "".format(rtc.name, rtc.max_speed, rtc.milege, rtc.color))

# Class Inheritance
rtc.seating_capacity(50)
print(rtc.seating_capacity(50))
