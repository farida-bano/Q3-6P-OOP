#6. Constructors and Destructors

#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created")

    def __del__(self):
        print("Logger object destroyed")


# Logger ka object create karain
logger_obj = Logger()

# Ab `logger_obj` ko explicitly delete karain ya program ka execution complete hone dein
del logger_obj  # Destructor ko manually call karne ka tareeqa

# Agar aap program terminate karte hain, to destructor automatically call hoga
