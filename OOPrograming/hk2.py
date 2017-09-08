class Car(object):
    def __init__(self, price=0, speed=0, mileage=0, fuel='empty'):
        self.price = price
        self.mileage = mileage
        self.fuel = fuel
        self.speed = speed
        self.tax = '15%' if self.price > 10000 else '12%'
        self.display_all()

    def display_all(self):
        print "Price:", self.price, "\nSpeed:", self.speed, "mph\nFuel:", self.fuel, "\nMileage:", self.mileage, "mpg\nTax:", self.tax
        print ''
        return self

car1 = Car(2000, 35, 15, 'full')
car2 = Car(12000, 65, 27)
car3 = Car(9500, 45, 60)
car4 = Car(18000, 85, 58, 'full')
car5 = Car(13000, 65, 50, 'full')
car6 = Car(8000, 55, 48)

