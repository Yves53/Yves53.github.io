class Bike(object):
    mile = 0

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed

    def display_info(self):
        print self.price
        print self.max_speed
        print Bike.mile
        return self

    def ride(self):
        Bike.mile += 10
        print 'riding', (Bike.mile)
        return self

    def reverse(self):
        Bike.mile -= 5
        print 'reversing', (Bike.mile)
        return self

bike1 = Bike(200, "25 mph")
Bike.mile = 50
bike1.ride().ride().ride().reverse().display_info()
bike1.ride().ride().ride().reverse().reverse().display_info()
bike1.reverse().reverse().reverse().display_info()
