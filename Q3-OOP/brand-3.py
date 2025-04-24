# 3. Public Variables and Methods

#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

# Main program flow
my_car = Car("Audi")  # Instantiate the Car class with "Audi"
print(my_car.brand)    # Access and print the brand of the car
my_car.start()         # Call the start method of the car