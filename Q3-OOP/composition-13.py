# 13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

# Create an Engine object
my_engine = Engine()

# Create a CarWithEngine object, passing the Engine instance
my_car = CarWithEngine(my_engine)

# Start the engine via the car
my_car.start_engine()  # This will print "Engine started"